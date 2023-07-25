import random

def calculate_absorption(sound_level, material, thickness):
    """Calculates the absorption of sound on multiple materials"""
    # Absorption coefficients for different materials (example values)
    absorption_coefficients = {
        'glass': 0.2,
        'wood': 0.4,
        'concrete': 0.6
    }

    # Check if the material is valid
    material_lower = material.lower()
    if material_lower not in absorption_coefficients:
        print("Invalid material!")
        return None

    # Get the absorption coefficient for the specified material
    absorption_coefficient = absorption_coefficients[material_lower]

    # Convert thickness from centimeters to meters
    thickness_meters = thickness / 100.0

    # Calculate the absorbed sound level using the Sabine formula
    absorbed_sound_level = sound_level + 10 * absorption_coefficient * thickness_meters

    return absorbed_sound_level


def calculate_attenuation(sound_level, distance, material, thickness):
    """Calculates the attenuation of sound over a certain distance"""
    # Attenuation factor for distance (example value)
    attenuation_factor = 0.1

    # Calculate distance attenuation
    distance_attenuation = sound_level - (distance * attenuation_factor)

    # Calculate absorbed sound level
    absorbed_sound_level = calculate_absorption(distance_attenuation, material, thickness)

    return absorbed_sound_level


def main():
    
    mower = input("Choose your lawnmower (gas / flail / electric): ").lower()
    
    lawn_mowers_sound = {
        "gas": random.randint(90, 96),
        "flail": random.randint(85, 100),
        "electric": random.randint(60, 75)
    }
    
    
    
    # Accept input sound level in decibels
    sound_level = lawn_mowers_sound[mower]

    # Accept the distance in meters
    distance = float(input("Enter the distance in meters: "))

    # Accept the material
    material = input("Enter the material (glass, wood, or concrete): ")
    
    #Accept thickness
    thickness = float(input("Enter the thickness of the material in centimeters: "))

    # Calculate absorbed sound level
    absorbed_sound_level = calculate_attenuation(sound_level, distance, material, thickness)

    if absorbed_sound_level is not None:
        # Print the output sound level
        print("Output sound level: {:.2f} dB".format(absorbed_sound_level))


if __name__ == '__main__':
    main()


# Give estimate of decibel values




# def main():
#     # Accept input sound level in decibels
#     sound_level = float(input("Enter the sound level in decibels: "))

#     # Accept the material
#     material = input("Enter the material (glass, wood, or concrete): ")

#     # Accept the thickness in centimeters
#     thickness = float(input("Enter the thickness of the material in centimeters: "))

#     # Calculate absorbed sound level
#     absorbed_sound_level = calculate_absorption(sound_level, material, thickness)

#     if absorbed_sound_level is not None:
#         # Print the output sound level
#         print("Output sound level: {:.2f} dB".format(absorbed_sound_level))


# if __name__ == '__main__':
#     main()
