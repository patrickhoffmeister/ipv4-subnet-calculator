# IPv4 Subnet-Rechner

Ein einfacher Subnetz-Rechner in Python zur Berechnung wichtiger Netzwerkparameter anhand einer IPv4-Adresse mit CIDR-Präfix.


Die Klasse **Ipadresse** zerlegt eine Eingabe wie

`192.168.1.100/24`

in **IPv4-Adresse** und **CIDR-Präfix** und berechnet, nach dem Validieren der IP-Adresse, daraus die entsprechenden Subnetzinformationen.


### Beispiel:

`10.12.77.180/21`

Gegeben:                        10.12.77.180/21
Subnetmaske:                 255.255.248.0
Netzadressen:       {
    'Netzadresse': '           10.12.72.0',
    'Broadcastadresse': '   10.12.79.255',
    'Nutzbare Hosts':        2046,
    'Blockgröße':               8
}



### Work in Progress
