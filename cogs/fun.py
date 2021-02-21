import discord
from discord.ext import commands, flags
from io import BytesIO


class Fun(commands.Cog):
    """For the fun commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='Sends a cat for every error code', aliases=['httpcat', 'http_cat'])
    async def http(self, ctx, code=404):
        async with self.bot.session.get(
                f"https://http.cat/{code}") as resp:
            buffer = await resp.read()
        embed = discord.Embed(colour=self.bot.embed_color, timestamp=ctx.message.created_at)
        embed.set_image(url=f"attachment://{code}.png")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, file=discord.File(BytesIO(buffer), filename=f"{code}.png"))

    @flags.add_flag("--dark", action='store_true', default=False)
    @flags.command(help='Makes a supreme logo from text')
    async def fakesupreme(self, ctx, text, **flags):
        await ctx.send(f'{text} {flags["dark"]}')


def setup(bot):
    bot.add_cog(Fun(bot))
