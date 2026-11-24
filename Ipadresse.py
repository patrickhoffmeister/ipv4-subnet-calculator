import re

class Ipadresse:
    def __init__(self, input_ip:str):
        if self.is_valid(input_ip):
            self.ip, cidr = input_ip.split("/")
            self.cidr = int(cidr)
        else:
            raise ValueError ("ungültige IP-Adresse")


    def is_valid(self, input_ip:str):
        pattern = r"^\d{1,3}(\.\d{1,3}){3}/\d{1,2}$"

        if not re.fullmatch(pattern, input_ip):
            return False
        
        ip, cidr = input_ip.split("/")
        if not 0 < int(cidr) <= 32:
            return False
        
        for oktett in ip.split("."):
            if not 0 <= int(oktett) < 256:
                return False
            
        return True


    def get_subnetmask(self):
        subnetzmaske = []
        cidr = self.cidr
        for _ in range(4):
            if cidr >= 8:
                subnetzmaske.append(255)
                cidr -= 8
            elif cidr > 0:
                subnetzmaske.append(256 - 2**(8-cidr))
                cidr = 0
            else:
                subnetzmaske.append(0)

        for _ in range(4-len(subnetzmaske)):
            subnetzmaske.insert(0, 255)
        return self.ipliste2string(subnetzmaske)


    def get_netzadressen(self):
        ip_liste = [int(x) for x in self.ip.split(".")]
        interessantes_oktett = self.cidr % 8
        oktett = self.cidr // 8 + 1
        blockgröße = 2 ** (8 - interessantes_oktett)
        nutzbare_hosts = 2**(32-self.cidr)-2
        na_name = "Netzadresse"
        bc_name = "Broadcastadresse"

        # Sonderfälle
        if self.cidr == 32:
            oktett = 4
            blockgröße = 1
            nutzbare_hosts = 1
            na_name = "Einzige Adresse"
            bc_name = "Einzige Adresse"
        elif self.cidr == 31:
            nutzbare_hosts = 2
            na_name = "Erste Adresse"
            bc_name = "Letzte Adresse"

        netzadresse = [ip_liste[oktett-1] // blockgröße * blockgröße]
        for i in range(int(oktett) -1):
            netzadresse.insert(i, ip_liste[i])

        while len(netzadresse) < 4:
            netzadresse.append(0)

        broadcastadresse = netzadresse.copy()
        broadcastadresse[oktett - 1] += blockgröße - 1
        for i in range(oktett, 4):
            broadcastadresse[i] = 255

        netzadresse = self.ipliste2string(netzadresse)
        broadcastadresse = self.ipliste2string(broadcastadresse)

        self.netzadressen = {
            f"{na_name}": netzadresse, 
            f"{bc_name}": broadcastadresse, 
            "Nutzbare Hosts": nutzbare_hosts, 
            "Blockgröße": blockgröße
        }
        return self.netzadressen


    def ipliste2string(self, ipliste:list):
        ipstring = ".".join([str(x) for x in ipliste])
        return ipstring


    def get_ip(self):
        return self.ip


    def get_cidr(self):
        return self.cidr

