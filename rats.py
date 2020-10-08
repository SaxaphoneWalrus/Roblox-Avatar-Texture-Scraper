import requests

def collect(user_id):
	user = requests.get(f'https://www.roblox.com/avatar-thumbnail-3d/json?userId={user_id}')
	hash = requests.get(user.json()['Url']).json()['textures'][0]

	i = 31
	for x in range(0,32):
		i ^= ord(hash[x])
		


	print(f'Avatar Texture for {user_id}: \nhttps://t{i%8}.rbxcdn.com/{hash}')
	input('\n\nPress enter to exit.')

id = input('ID of user you want the avatar texture of: \n')
collect(id)