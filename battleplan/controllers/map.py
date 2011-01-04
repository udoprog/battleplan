import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from battleplan.lib.base import BaseController, render
from battleplan import model as m
from battleplan.lib import jumps, systems

log = logging.getLogger(__name__)

class MapController(BaseController):
    @jsonify
    def systems(self):
        q = m.Session.query(m.SolarSystem).filter(m.SolarSystem.constellationID < 21000000);
        
        if "region" in request.params:
            q = q.filter(m.SolarSystem.regionID == int(request.params.get("region")))
        
        if "constellation" in request.params:
            q = q.filter(m.SolarSystem.constellationID == int(request.params.get("constellation")))
        
        res = int(request.params.get("resolution", 1024))
        
        map_systems = list(q.all())
        
        if len(map_systems) == 0:
            return {'systems': [], 'jumps': []}
        
        max_x = None
        max_z = None
        min_x = None
        min_z = None
        not_set = True
        
        for s in map_systems:
            if not_set:
                max_x = s.x
                max_z = s.z
                min_x = s.x
                min_z = s.z
                not_set = False
                continue
            
            max_x = max(s.x, max_x)
            max_z = max(s.z, max_z)
            min_x = min(s.x, min_x)
            min_z = min(s.z, min_z)
        
        result_systems = dict()

        diff_x = (max_x - min_x)
        diff_z = (max_z - min_z)

        res_x = res
        res_z = res
        extra_x = 0
        extra_z = 0

        if diff_x > diff_z:
            res_z = diff_z / diff_x * res
            extra_z = (res - res_z) / 2
        else:
            res_x = diff_x / diff_z * res
            extra_x = (res - res_x) / 2

        def _add_system(s):
            return {
                'security': int(round(s.security * 10.0)),
                'name': s.solarSystemName,
                'x': int((s.x - min_x) / (max_x - min_x) * res_x + extra_x),
                'z': int((s.z - min_z) / (max_z - min_z) * res_z + extra_z)
            }
        
        for s in map_systems:
            result_systems[s.solarSystemID] = _add_system(s)
        
        result_jumps = list()
        visited_jumps = set()
        
        for s_id, _ in result_systems.items():
            # does the current system even have available jumps?
            if s_id not in jumps:
                continue
            
            for j in jumps[s_id]:
                in_coll = True
                
                jump_id = (s_id, j)
                
                # is this jump already recorded?
                if jump_id in visited_jumps:
                    continue
                
                # lookup the target system
                s = systems[j]
                
                # is this a jump over the edge?
                if s.solarSystemID not in result_systems:
                    in_coll = False
                    result_systems[s.solarSystemID] = _add_system(s)
                
                jump_id_rev = (j, s_id)
                
                # record the jump in both directions
                visited_jumps.add(jump_id)
                visited_jumps.add(jump_id_rev)
                
                result_jumps.append((jump_id[0], jump_id[1], in_coll))
        
        return {'systems': result_systems, 'jumps': result_jumps}
