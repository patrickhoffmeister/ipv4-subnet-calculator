import Ipadresse as IP


eingabe = input("Gib eine IPv4 Adresse ein. Format '10.12.77.180/21': ")


ipadresse = IP.Ipadresse(eingabe)


subnetzmaske = ipadresse.get_subnetmask()
netzadressen = ipadresse.get_netzadressen()


print(f"Gegeben:            {ipadresse.get_ip()}/{ipadresse.get_cidr()}")
print(f"Subnetmaske:        {subnetzmaske}")
print(f"Netzadressen:       {netzadressen}")
