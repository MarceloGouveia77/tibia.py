import asynctest
from aioresponses import aioresponses

from tests.tests_character import FILE_CHARACTER_RESOURCE, FILE_CHARACTER_NOT_FOUND
from tests.tests_guild import FILE_GUILD_FULL, FILE_GUILD_LIST
from tests.tests_highscores import FILE_HIGHSCORES_FULL
from tests.tests_house import FILE_HOUSE_FULL, FILE_HOUSE_LIST
from tests.tests_tibiapy import TestCommons
from tibiapy import Client, Character, Guild, Highscores, VocationFilter, Category, House, ListedHouse, ListedGuild


class TestClient(asynctest.TestCase, TestCommons):
    def setUp(self):
        self.client = Client()

    async def tearDown(self):
        await self.client.session.close()

    @aioresponses()
    async def testFetchCharacter(self, mock):
        name = "Tschas"
        content = self._load_resource(FILE_CHARACTER_RESOURCE)
        mock.get(Character.get_url(name), status=200, body=content)
        character = await self.client.fetch_character(name)

        self.assertIsInstance(character, Character)

    @aioresponses()
    async def testFetchCharacterNotFound(self, mock):
        name = "Nezune"
        content = self._load_resource(FILE_CHARACTER_NOT_FOUND)
        mock.get(Character.get_url(name), status=200, body=content)
        character = await self.client.fetch_character(name)

        self.assertIsNone(character)

    @aioresponses()
    async def testFetchGuild(self, mock):
        name = "Vitam et Mortem"
        content = self._load_resource(FILE_GUILD_FULL)
        mock.get(Guild.get_url(name), status=200, body=content)
        guild = await self.client.fetch_guild(name)

        self.assertIsInstance(guild, Guild)

    @aioresponses()
    async def testFetchGuildList(self, mock):
        world = "Zuna"
        content = self._load_resource(FILE_GUILD_LIST)
        mock.get(ListedGuild.get_world_list_url(world), status=200, body=content)
        guilds = await self.client.fetch_world_guilds(world)

        self.assertIsInstance(guilds[0], ListedGuild)

    @aioresponses()
    async def testFetchHighscores(self, mock):
        world = "Estela"
        category = Category.MAGIC_LEVEL
        vocations = VocationFilter.KNIGHTS
        content = self._load_resource(FILE_HIGHSCORES_FULL)
        mock.get(Highscores.get_url(world, category, vocations), status=200, body=content)
        highscores = await self.client.fetch_highscores_page(world, category, vocations)

        self.assertIsInstance(highscores, Highscores)

    @aioresponses()
    async def testFetchHouse(self, mock):
        world = "Antica"
        house_id = 5236
        content = self._load_resource(FILE_HOUSE_FULL)
        mock.get(House.get_url(house_id, world), status=200, body=content)
        house = await self.client.fetch_house(house_id, world)

        self.assertIsInstance(house, House)

    @aioresponses()
    async def testFetchHouseList(self, mock):
        world = "Antica"
        city = "Edron"
        content = self._load_resource(FILE_HOUSE_LIST)
        mock.get(ListedHouse.get_list_url(world, city), status=200, body=content)
        houses = await self.client.fetch_world_houses(world, city)

        self.assertIsInstance(houses, list)
        self.assertIsInstance(houses[0], ListedHouse)
