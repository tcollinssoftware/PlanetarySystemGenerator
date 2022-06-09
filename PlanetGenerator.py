import random

running = True

while running == True:

	def input_phase():
		print('##########')
		print('What would you like to do?')
		user_inp = input()
		if user_inp == 'generate':
			print('##########')
			generate_bodies()
		if user_inp == 'quit':
			quit()
		if user_inp != 'quit' and user_inp != 'generate':
			print('Invalid command.')
			input_phase()


	def start():
		print('Welcome to my Planet Generator.')
		print("Input 'generate' to generate a new planet, or type 'quit' to exit the program.")
		input_phase()

	def generate_name():
		name_parts_max = 2
		name_length_min = 3
		name_length_max = 14
		vowels = ['a', 'e', 'i', 'o', 'u', 'y']
		consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
		special_characters = ["'", '-', ' ']
		name_parts = random.randint(1, 2)
		previous_character = 'NONE'
		name_list = []
		if name_parts == 1:
			name_1_length = random.randint(name_length_min,name_length_max)
			for i in range(name_1_length):
				if previous_character == 'NONE':
					vowel_or_cons = random.randint(0, 1)
					if vowel_or_cons == 0:
						name_list.append(random.choice(vowels))
						previous_character = 'vowel'
						continue
					if vowel_or_cons == 1:
						name_list.append(random.choice(consonants))
						previous_character = 'consonant'
						continue
				if previous_character == 'vowel':
					chance_of_duplicate_char_type = random.randint(1, 4)
					if chance_of_duplicate_char_type <= 1:
						name_list.append(random.choice(vowels))
						previous_character = 'vowel'
						continue
					else:
						name_list.append(random.choice(consonants))
						previous_character = 'consonant'
						continue
				if previous_character == 'consonant':
					chance_of_duplicate_char_type = random.randint(1, 4)
					if chance_of_duplicate_char_type <= 1:
						name_list.append(random.choice(consonants))
						previous_character = 'consonant'
						continue
					else:
						name_list.append(random.choice(vowels))
						previous_character = 'vowel'
						continue

		if name_parts == 2:
			name_length = random.randint(7, name_length_max)
			division_point = random.randint(name_length_min + 1, name_length - 3)
			name_1_length = division_point - 1
			name_2_length = name_length - division_point
			for i in range(name_length):
				if i == division_point:
					name_list.append(random.choice(special_characters))
					previous_character = 'NONE'
					continue
				if previous_character == 'NONE':
					vowel_or_cons = random.randint(0, 1)
					if vowel_or_cons == 0:
						name_list.append(random.choice(vowels))
						previous_character = 'vowel'
						continue
					if vowel_or_cons == 1:
						name_list.append(random.choice(consonants))
						previous_character = 'consonant'
						continue
				if previous_character == 'vowel':
					chance_of_duplicate_char_type = random.randint(1, 4)
					if chance_of_duplicate_char_type <= 1:
						name_list.append(random.choice(vowels))
						previous_character = 'vowel'
						continue
					else:
						name_list.append(random.choice(consonants))
						previous_character = 'consonant'
						continue
				if previous_character == 'consonant':
					chance_of_duplicate_char_type = random.randint(1, 4)
					if chance_of_duplicate_char_type <= 1:
						name_list.append(random.choice(consonants))
						previous_character = 'consonant'
						continue
					else:
						name_list.append(random.choice(vowels))
						previous_character = 'vowel'
						continue
		num_consecutive_consonants = 0
		for idx, val in enumerate(name_list):
			if val in consonants:
				num_consecutive_consonants += 1
				if num_consecutive_consonants == 3:
					name_list[idx - 1] = random.choice(vowels)
					num_consecutive_consonants = 0
			else:
				num_consecutive_consonants = 0

		if name_list[0] in consonants and name_list[1] in consonants:
			name_list[0] = random.choice(vowels)

		first_letter = name_list[0].upper()
		name_list[0] = first_letter

		for idx, val in enumerate(name_list):
			if val in special_characters:
				second_capital = name_list[idx + 1].upper()
				name_list[idx + 1] = second_capital

		planet_name = ''
		for i in name_list:
			planet_name += i

		return (planet_name)

	def generate_bodies():
		planet_prime_name = generate_name()
		moon_list = []
		planet_types = ['Earth-Like', 'Dwarf Planet', 'Gas Giant', 'Ice Giant', 'Super Planet']
		planet_type = random.choice(planet_types)

		if planet_type == 'Earth-Like':
			size = random.uniform(0.5, 5.0)
			moon_count = random.randint(0, 3)

		if planet_type == 'Dwarf Planet':
			size = random.uniform(0.1, 0.5)
			moon_count = random.randint(0,2)

		if planet_type == 'Gas Giant' or planet_type == 'Ice Giant':
			size = random.uniform(10.0, 30.0)
			moon_count = random.randint(0, 22)

		if planet_type == 'Super Planet':
			size = random.uniform(5.0, 12.0)
			moon_count = random.randint(0,6)

		ring_count = random.randint(0,3)

		print('Planet Name : ' + planet_prime_name)
		print('Planet Type : ' + planet_type)
		print('Size : ' + str(round(size, 2)) + ' Earths')

		if moon_count <= 5:
			for i in range(moon_count):
				x = generate_name()
				moon_list.append(x)

		if moon_count > 5:
			for i in range(moon_count):
				x = i + 1
				val = [
					1000, 900, 500, 400,
					100, 90, 50, 40,
					10, 9, 5, 4,
					1
				]
				syb = [
					"M", "CM", "D", "CD",
					"C", "XC", "L", "XL",
					"X", "IX", "V", "IV",
					"I"
				]
				roman_num = ''
				i_num = 0
				while x > 0:
					for _ in range(x // val[i_num]):
						roman_num += syb[i_num]
						x -= val[i_num]
					i_num += 1
				moon_list.append(planet_prime_name + ' ' + roman_num)

		if moon_count >= 1:
			moons_string = ''
			for i in moon_list:
				if i != moon_count:
					moons_string += i + ', '
				if i == moon_count:
					moons_string += i
			moons_string_size = len(moons_string)
			moons_string = moons_string[:moons_string_size - 2]
			print('Moon Count : ' + str(moon_count))
			if moon_count == 1:
				print('Moon : ' + moons_string)
			if moon_count > 1:
				print('Moons : ' + moons_string)
		if moon_count == 0:
			print('No Moons')
		generate_composition(planet_type)

	def generate_composition(planet_type):
		colors = [
			'Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue',
			'Magenta', 'Purple', 'White', 'Black', 'Gray', 'Silver,'
			'Pink', 'Maroon', 'Brown', 'Beige', 'Tan', 'Peach',
			'Lime', 'Olive', 'Turquoise', 'Teal', 'Navy', 'Indigo',
			'Violet'
		]

		sky_color = random.choice(colors)
		predominant_flora_color = random.choice(colors)

		terrain_varieties = [
			'Rain Forest', 'Temperate Forest', 'Jungle', 'Desert',
			'Tundra', 'Taiga', 'Grassland', 'Savanna', 'Aquatic', 'Ice',
			'Badland', 'Salt Flat', 'Hill', 'Mountain', 'Cliff',
			'Massif', 'Crystal Desert', 'Molten', 'Highland'
		]

		terrain_varieties_wo_aquatic = [
			'Rain Forest', 'Temperate Forest', 'Jungle', 'Desert',
			'Tundra', 'Taiga', 'Grassland', 'Savanna', 'Ice',
			'Badland', 'Salt Flat', 'Hill', 'Mountain', 'Cliff',
			'Massif', 'Crystal Desert', 'Molten', 'Highland'
		]

		terrain_varieties_ice = [
			'Tundra', 'Taiga', 'Ice', 'Salt Flat', 'Hill', 'Mountain',
			'Cliff', 'Massif', 'Crystal Desert', 'Aquatic'
		]

		terrain_varieties_ice_wo_aquatic = [
			'Tundra', 'Taiga', 'Ice', 'Salt Flat', 'Hill', 'Mountain',
			'Cliff', 'Massif', 'Crystal Desert'
		]

		terrain_count = random.randint(1, 5)
		terrain_types = []
		temp_terrain_count = terrain_count
		#set chosen terrain to variable, check if variable is in list, if it is, choose a different one
		if planet_type != 'Gas Giant':
			if terrain_count > 1:
				has_ocean = random.randint(0, 3)
				if has_ocean != 3:
					terrain_types.append('Aquatic')
					temp_terrain_count -= 1

			terrain_variety_set = set(terrain_varieties)
			terrain_variety_wo_aquatic_set = set(terrain_varieties_wo_aquatic)
			terrain_variety_ice_set = set(terrain_varieties_ice)
			terrain_variety_ice_wo_aquatic_set = set(terrain_varieties_ice_wo_aquatic)

			if terrain_types:
				if planet_type != 'Ice Giant':
					terrain_types += random.choices(list(terrain_variety_set), k = terrain_count - 1)
				if planet_type == 'Ice Giant':
					terrain_types += random.choices(list(terrain_variety_ice_set), k=terrain_count - 1)

			if not terrain_types:
				if planet_type != 'Ice Giant':
					terrain_types = random.choices(list(terrain_variety_wo_aquatic_set), k = terrain_count)
				if planet_type == 'Ice Giant':
					terrain_types = random.choices(list(terrain_variety_ice_wo_aquatic_set), k=terrain_count)

			terrain_string = ''
			for i in terrain_types:
				terrain_string += i + ', '
			terrain_string_size = len(terrain_string)
			terrain_string = terrain_string[:terrain_string_size - 2]

		if planet_type == 'Gas Giant':
			terrain_types.append('Gas')
			terrain_string = ''
			for i in terrain_types:
				terrain_string += i

		print('Sky Color : ' + sky_color)
		print('Biomes : ' + terrain_string)
		print('Predominant Flora Color : ' + predominant_flora_color)


		generate_cycles(planet_type)


	def generate_cycles(planet_type):

		temperature_low = float()
		temperature_high = float()
		habitability_types = ['Ideal', 'Moderate', 'Hostile', 'Extreme', 'Uninhabitable']

		atmospheric_conditions = ['Ideal', 'Sickening', 'Poisonous']
		atmosphere_type = random.choice(atmospheric_conditions)

		if planet_type == 'Ice Giant':
			temperature_low = random.uniform(-53, -22)
			temperature_high = random.uniform(-21, 10)
			if temperature_low < -44:
				habitability = 'Uninhabitable'
			if temperature_low >= -44 and temperature_low < -35:
				habitability = 'Extreme'
			if temperature_low >= -35 and temperature_low < -26:
				habitability = 'Hostile'
			if temperature_low >= -26 and temperature_low <= -22:
				habitability = 'Moderate'

		if planet_type != 'Ice Giant': #-300f to +800f #temp should determine habitability
			habitability = random.choice(habitability_types)

			hot_or_cold = random.randint(0, 1) #0 if cold, 1 if hot

			if habitability == 'Ideal':
				temperature_low = random.uniform(-17, 58)
				temperature_high = random.uniform(59,100)
			if habitability == 'Moderate':
				if hot_or_cold == 0:
					temperature_low = random.uniform(-26, -22)
					temperature_high = random.uniform(-21, -17)
				if hot_or_cold == 1:
					temperature_low = random.uniform(100, 125)
					temperature_high = random.uniform(126, 150)
			if habitability == 'Hostile':
				if hot_or_cold == 0:
					temperature_low = random.uniform(-35, -31)
					temperature_high = random.uniform(-30, -26)
				if hot_or_cold == 1:
					temperature_low = random.uniform(150, 175)
					temperature_high = random.uniform(176, 200)
			if habitability == 'Extreme':
				if hot_or_cold == 0:
					temperature_low = random.uniform(-44, -40)
					temperature_high = random.uniform(-39, -35)
				if hot_or_cold == 1:
					temperature_low = random.uniform(200, 225)
					temperature_high = random.uniform(226, 250)
			if habitability == 'Uninhabitable':
				if hot_or_cold == 0:
					temperature_low = random.uniform(-53, -49)
					temperature_high = random.uniform(-48, -44)
				if hot_or_cold == 1:
					temperature_low = random.uniform(250, 275)
					temperature_high = random.uniform(276, 300)

		temp_low_round = round(temperature_low, 2)
		temp_high_round = round(temperature_high, 2)

		if atmosphere_type == 'Ideal': #if ideal, temperature determines habitability
			pass
		if atmosphere_type == 'Sickening': #if sickening, if habitability is below hostile, set to hostile
			if habitability == 'Moderate' or habitability == 'Ideal':
				habitability = 'Hostile'
		if atmosphere_type == 'Poisonous': #if poisonous, if habitability is below extreme, set to extreme
			if habitability == 'Hostile' or habitability == 'Moderate' or habitability == 'Ideal':
				habitability = 'Extreme'

		print('Atmosphere : ' + atmosphere_type)
		print('Low Temperature : ' + str(temp_low_round) + 'F')
		print('High Temperature : ' + str(temp_high_round) + 'F')
		print('Habitability : ' + habitability)

		day_length = random.randint(8, 300)
		year_length = random.randint(60, 3000)

		print('Day Length : ' + str(day_length) + ' Hours')
		print('Year Length : ' + str(year_length) + ' Days')

		generate_civilizations(habitability)

	def generate_civilizations(habitability):
		inhabited = 0


		if habitability != 'Uninhabitable':

			inhabited = random.randint(0, 1)
			if inhabited == 1:
				allegiances = ['Republic', 'Empire', 'Independent']

				native_sentient_species = generate_name()
				unified = random.randint(0, 1) #0 for no, 1 for yes
				major_faction_count = random.randint(2, 8)
				majority_allegiance = random.choice(allegiances)

				print('Native Sentient Species : ' + native_sentient_species)

				if unified == 0:
					print('Unified : No')
				if unified == 1:
					print('Unified : Yes')

				print('Major Factions : ' + str(major_faction_count))
				print('Majority Allegiance : ' + majority_allegiance)

			if inhabited == 0:
				print('Planet Uninhabited')

		if habitability == 'Uninhabitable':
			print('Planet Uninhabited')

		input_phase()

	start()