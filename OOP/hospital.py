
class Patient(object):
    pt_total = 0
    def __init__(self, names, allergies):
        self.id_num = Patient.pt_total
        self.names = names
        self.allergies = allergies
        self.bed_num = None
        Patient.pt_total += 1

    def info(self):
        print "Patient ID: " + str(self.id_num)
        print "Patient Name: " + self.names
        print "Patient Allergies: " + self.allergies
        print ""
        return self

class Hospital(object):

    def __init__(self):
        self.hosp_name = "Regan Memorial"
        self.capacity = 10
        self.patients = []
        self.beds = self.pt_beds()

    def pt_beds(self):
        beds = []
        for i in range(0, self.capacity):
            beds.append({
                "bed_num": i,
                "vacant": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) <= self.capacity:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["vacant"]:
                    patient.bed_num = self.beds[i]["bed_num"]
                    self.beds[i]["vacant"] = False
                    break
            print "Patient #" + str(patient.id_num) + ", " + str(patient.names) + "," " admitted to bed #" + str(patient.bed_num)
        else:
            print "Hospital is at full capacity"
        return self

    def discharge(self,pt_id):
        for patient in self.patients:
            if patient.id_num == pt_id:
                for bed in self.beds:
                    if bed["bed_num"] == patient.bed_num:
                        bed["vacant"] = True
                        break
                self.patients.remove(patient)
            print "Patient #" + str(patient.id_num) + ", " + str(patient.names) + "," + " discharged. Bed #" + str(patient.bed_num) + " now available"
        return self

    def display(self):
        print "Hospital: " + self.hosp_name
        print "Max Capacity: " + str(self.capacity)
        print ""
        return self

patient1 = Patient("Robert Amato", "asprin")
patient1.info()

patient2 = Patient("Maggie Amato", "none")
patient2.info()

patient3 = Patient("Kim Amato", "none")
patient3.info()

patient4 = Patient("Franklin Amato", "shellfish")
patient4.info()

patient5 = Patient("Ashley Amato", "morphine")
patient5.info()

p2 = Hospital()
p2.display().admit(patient1)

p3 = Hospital()
p3.display().admit(patient2).admit(patient3).admit(patient4)

p4 = Hospital()
p4.display().admit(patient5)
p4.discharge(patient1)
