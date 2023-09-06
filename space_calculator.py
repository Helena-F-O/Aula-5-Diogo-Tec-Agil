class Converter:

  def converter_massa_lunar(self, quilogramas):
    # Aproximadamente 1 kg na Terra é equivalente a 0,1653 kg na Lua
    massa_lunar = quilogramas * 0.1653
    return massa_lunar

  def converter_distancia_marte(self, metros):
    # Aproximadamente 1 metro na Terra é equivalente a 0,3773 metros em Marte
    distancia_marte = metros * 0.3773
    return distancia_marte
