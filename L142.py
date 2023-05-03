#Emily Nixon and Katie O'Rourke
class ambulance:
    """An object with dimensions.
    Attributes: Height, siren, color, width, patient capacity, speed"""

ambulance.height =  "7 feet"
ambulance.siren = "Shrill"
ambulance.color = "White and Red"
ambulance.width ="15 feet"
ambulance.patients = 3
ambulance.traffspeed = 45


def speed(patients):
    if patients.patients > 0:
        speed = 2.3*(patients.patients-0.5)*ambulance.traffspeed+30*(patients.patients-2.143)
    else:
        speed = ambulance.traffspeed
    print(speed)

speed(ambulance)

ambulance.patients = 0
speed(ambulance)
