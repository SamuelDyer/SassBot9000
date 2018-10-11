import discord
from discord.ext import commands
import asyncio
import random
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix= ("~", "!", "?"))

client = discord.Client()

@bot.event
async def on_ready():
         print("Verification for me")
         print (bot.user.id)
         print('Im finally here')

@bot.command(pass_context=True)
async def commands(cxt):
    await bot.say("~commands, ~mood, ~sigh, ~OwO, ~dadjoke, ~8ball, ~prefixes")

@bot.command(pass_context=True)
async def mood(cxt):
    await bot.say("Thats a Mood")

@bot.command(pass_context=True)
async def sigh(cxt):
    await bot.say(":sigh:")

@bot.command(pass_context=True)
async def OwO(cxt):
    await bot.say(":OwO:")

@bot.command(name='dadjoke',
				description="Tells you a dadjoke.",
				brief="Makes you cringe/laugh.",
				aliases=['Dad_Joke', 'DadJoke', 'dad_joke'],
				pass_context=True)
async def dadjoke(cxt):
	possible_responses = [
		'So, why did 7 eat 9? Because youre supposed to eat 3 square meals a day',
		'I tell a lot of desert jokes... i must have a dry sense of humor',
		'Two fishs are in a tank, one of them says to the other "so how do i drive this thing"',
		'what is the best season to sell Life Alert? Fall',
		'"But Dad I dont want to see grandma!""Shut up and keep digging"',
		'What Does Cardi B do to lose weight? Cardi O',
		'One of my coworkers told me they had blood drawn, I asked if it was in pencil or crayon',
		'Im always running behind schedule, Hes a fast guy i just cant seem to keep up',
		'To the guy who invented zero...Thanks for nothing',
		'Whats Owen Wilsons favorite game to play? WoW',
		'I once sat down on a sheet of glass, It was a massive pain in the ass',
		'What do you call a blind deer? No idea',
		'Theres lots of options when buying tape. Youve got painters tape, duct tape, but I think transparent tape is the clear winner',
		'Saw a guy standing on one leg at an atm. Confused, i asked him what he was going he said he was just checking his balance',
		'I called the paranoia hotline A guy answerd "How the hell did you get this number?',
		'1S2A3F4E5T6Y7 safety in numbers',
		'Research has shown that 6 out of 7 dwarfs are happy',
		'What cant t-rex clap their hands? because they are extinct...',
		'What do you call a dwarf psychic on the run from the law? A small medium at large',
		'When Usain Bolt started runiing the 200m in addition to his 100m sprint His career finally turned a corner',
		'I opened a fortune cookie to find no fortune, Dad "Well thats unfortuneate',
		'Two wrongs dont make a right, But three rights make a left',
		'I believe the 2020 election will come down to one deciding factor: What candidate has the best vision',
		'Who invented the cross walk? Jesus Christ',
		'A blind guy walks into a bar, "OW" He exclaimed',
		'Who is this? No, Who isnt this?',
		'Life is like a unfinished joke',
		'My girlfreind told me i was stupid, I told her she was clever in her own way',
		'My wife handed me two kayak paddles and asked me which one I wanted, i replyed with "either, oar"',
		'What do you call a Mexican who lost his car? Carlos',
		'There are three types of people. Ones that can count, Ones that cant.',
		'Someone asked me if I knew what Campanlogy was. I replied with "It rings a bell',
		'To whoever has my Office 365 product key. I will find you, you have my word',
		'Dad, i found a penny in the bathtub. That makes no sense. "That doesnt make no cents, it makes one cent',
		'What did the bra say to the hat? "You go ahead, i can lift these two',
		'How many birds does it take to screw in a lightbulb? Preferbly Three, but Toucan',
	]

	await bot.say(random.choice(possible_responses))

@bot.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(cxt):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]

    await bot.say(random.choice(possible_responses))

@bot.command(pass_context=True)
async def prefixes(cxt):
	await bot.say("The prefixes that you can use for this bot include ~,!,?")

@bot.command(pass_context=True)
async def ():
	pass

bot.run(TOKEN)