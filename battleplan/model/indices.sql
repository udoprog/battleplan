-- This file contains a set of mysql indices
-- I am a bit rusty on mysql atm, so I have to check a lot of things up

-- mapped index on solarsystem name to improve lookup performance
drop index solarSystemName_Index on mapSolarSystems;
create index solarSystemName_Index on mapSolarSystems(solarSystemName(5));

-- mapped index on hashes to allow for faster text searches
drop index name_Index on hashes;
create index name_Index on hashes(name(5));


