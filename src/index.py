from varasto import Varasto

def luonnin_jalkeen(mehu, olut):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehu}")
    print(f"Olutvarasto: {olut}")

def olut_getterit(olut):
    print("Olut getterit:")
    print(f"saldo = {olut.saldo}")
    print(f"tilavuus = {olut.tilavuus}")
    print(f"paljonko_mahtuu = {olut.paljonko_mahtuu()}")

def mehu_setterit(mehu):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehu.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehu}")
    print("Otetaan 3.14")
    mehu.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehu}")

def virheetilanteita():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def varastointi(mehua,olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def varastointi2(mehua,olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    luonnin_jalkeen(mehua, olutta)
    olut_getterit(olutta)
    mehu_setterit(mehua)
    virheetilanteita()
    varastointi(mehua, olutta)
    varastointi2(mehua, olutta)

if __name__ == "__main__":
    main()
