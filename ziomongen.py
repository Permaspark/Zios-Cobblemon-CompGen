def run_generator():
    def get_lowercase_input(prompt):
        while True:
            user_input = input(prompt).strip()
            if user_input.isalpha() and user_input.islower():
                return user_input
            elif user_input.isdigit():
                print("Invalid input. Please enter a valid lowercase string, not a number.")
            else:
                print("Invalid input. Please enter a valid lowercase string.")
    
    def get_ev_input(stat_name, current_total):
        while True:
            try:
                ev_value = int(input(f'Enter desired {stat_name} EV: ') or 0)
                if ev_value > 252:
                    print(f"Invalid {stat_name} EV value. It cannot exceed 252. Please enter a valid value.")
                elif current_total + ev_value > 510:
                    print(f"The total EVs would exceed 510 with {stat_name} EV. Please enter a smaller value.")
                else:
                    return ev_value
            except ValueError:
                print("Invalid input. Please enter a valid integer for EV values.")
    
    print('Hello! Thank you for using my Competitive Pokemon generator. Please visit https://github.com/Permaspark/Zios-Cobblemon-CompGen/issues for any problems.')
    pokemon = get_lowercase_input('Enter a Pokemon name (lowercase): ')
    attack_iv = int(input('Enter your preferred attack IV: ') or 0)
    speed_iv = int(input('Enter your preferred speed IV: ') or 0)
    
    nature = get_lowercase_input('Enter your preferred nature (lowercase): ')
    ability = get_lowercase_input('Enter your preferred ability (lowercase): ')

    total_evs = 0

    hp_ev = get_ev_input('hp', total_evs)
    total_evs += hp_ev

    attack_ev = get_ev_input('attack', total_evs)
    total_evs += attack_ev

    special_attack_ev = get_ev_input('special attack', total_evs)
    total_evs += special_attack_ev

    defense_ev = get_ev_input('defense', total_evs)
    total_evs += defense_ev

    special_defense_ev = get_ev_input('special defense', total_evs)
    total_evs += special_defense_ev

    speed_ev = get_ev_input('speed', total_evs)
    total_evs += speed_ev

    if total_evs > 510:
        print('Invalid EV count: The total EVs cannot exceed 510.')
    else:
        command = f'/pokegive {pokemon} level=100 ability={ability} nature={nature} attack_iv={attack_iv} speed_iv={speed_iv} hp_iv=31 defence_iv=31 special_defence_iv=31 special_attack_iv=31'

        if hp_ev > 0:
            command += f' hp_ev={hp_ev}'
        if attack_ev > 0:
            command += f' attack_ev={attack_ev}'
        if special_attack_ev > 0:
            command += f' special_attack_ev={special_attack_ev}'
        if defense_ev > 0:
            command += f' defence_ev={defense_ev}'
        if special_defense_ev > 0:
            command += f' special_defence_ev={special_defense_ev}'
        if speed_ev > 0:
            command += f' speed_ev={speed_ev}'

        print(command)

    restart = input('Would you like to start again? (Y/N): ').strip().lower()
    if restart == "y":
        run_generator()
    else:
        print("Bye bye!")

run_generator()
