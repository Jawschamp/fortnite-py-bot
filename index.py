# IMPORTANT
# To use this bot you must have Python 3.5 or higher
# Run 'py -3 -m pip install fortnitepy', "py -3 -m pip install json" to install required things
# Change the details, email, password, netcl, build, enginebuild in the __init__
import fortnitepy
import json

with open('config.json') as json_data_file:
    cfg = json.load(json_data_file)

class MyClient(fortnitepy.Client):
    def __init__(self):
        super().__init__(
            email=cfg.email,
            password=cfg.password,
            platform='cfg.platform,
            net_cl=cfg.netcl,
            build=cfg.build,
            engine_build=cfg.enginebuild,
            status=cfg.status
        )

    @client.event
    async def event_ready(self):
        print('----------------')
        print('Client ready as')
        print(self.user.display_name)
        print(self.user.id)
        print('----------------')

    @client.event
    async def event_friend_request(self, request):
        await request.accept()

    @client.event
    async def event_party_invite(invitation):
        await invitation.accept()

        # Purple skull trooper (ya'll wanted it :/ )
        variants = client.user.party.me.create_variants(
            clothing_color=1
        )
        await client.user.party.me.set_outfit(
            asset='CID_030_Athena_Commando_M_Halloween',
            variants=variants
            )

        # Skull Brite backpack
        await set_backpack('BID_211_SkullBrite', key=None)

        #
        await set_pickaxe('Pickaxe_ID_109_SkullTrooper', key=None)

        # Floss
        await set_emote('EID_Floss', run_for=None, key=None, section=None)

        # EG Banner
        await set_banner(icon='otherbanner28', color='defaultcolor', season_level=100)

        # BP
        await set_battlepass_info(has_purchased=true, level=9999999999, self_boost_xp=9999999999, friend_boost_xp=9999999999)

        # await invite(user_id) (Invite other bots/people to your lobby when the main bot joins.)

    @client.event
    async def event_friend_message(self, message):
    args = message.content.split(" ")
        if "CID_" in args[0]:
        await set_outfit(args[0])
        await message.reply('Skin set to ' + args[0])

        if "BID_" in args[0]:
        await set_backpack(args[0])
        await message.reply('Backpack set to ' + args[0])

        if "EID_" in args[0]:
        await set_emote(args[0])
        await message.reply('Emote set to ' + args[0])

        if "Pickaxe_ID_" in args[0]:
        await set_pickaxe(args[0])
        await message.reply('Emote set to ' + args[0])

        if args[0] == "!leave":
            await leave()
            await message.reply('Left party.')

        if args[0] == "!ready":
            await set_ready(true)
            await message.reply('Set ready to true. Note: This does not allow the bot to enter the game.')

        if args[0] == "!unready":
            await set_ready(false)
            await message.reply('Set ready to false. Note: This does not allow the bot to enter the game.')

        if args[0] == "!stop":
            await clear_emote()
            await message.reply('Cleared emote.')

        if args[0] == "!purpleskull":

            variants = client.user.party.me.create_variants(
            clothing_color=1
            )

            await client.user.party.me.set_outfit(
            asset='CID_030_Athena_Commando_M_Halloween',
            variants=variants
            )

    @client.event
    async def event_party_message(self, message):
        args = message.content.split(" ")
            if "CID_" in args[0]:
            await set_outfit(args[0])
            await message.reply('Skin set to ' + args[0])

            if "BID_" in args[0]:
            await set_backpack(args[0])
            await message.reply('Backpack set to ' + args[0])

            if "EID_" in args[0]:
            await set_emote(args[0])
            await message.reply('Emote set to ' + args[0])

            if "Pickaxe_ID_" in args[0]:
            await set_pickaxe(args[0])
            await message.reply('Emote set to ' + args[0])

            if args[0] == "!leave":
                await leave()

            if args[0] == "!ready":
                await set_ready(true)
                await message.reply('Set ready to true. Note: This does not allow the bot to enter the game.')

            if args[0] == "!unready":
                await set_ready(false)
                await message.reply('Set ready to false. Note: This does not allow the bot to enter the game.')

            if args[0] == "!stop":
                await clear_emote()
                await message.reply('Cleared emote.')

            if args[0] == "!purpleskull":

                variants = client.user.party.me.create_variants(
                clothing_color=1
                )

                await client.user.party.me.set_outfit(
                asset='CID_030_Athena_Commando_M_Halloween',
                variants=variants
                )

client = MyClient()
client.run()
