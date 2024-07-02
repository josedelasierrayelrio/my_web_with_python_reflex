import datetime

class Utils:

    @staticmethod
    def calcular_anios_experiencia(anio_inicio, mes_inicio):
        fecha_actual = datetime.datetime.now()
        anio_actual = fecha_actual.year
        mes_actual = fecha_actual.month
        anio_inicio = int(anio_inicio)
        mes_inicio = int(mes_inicio)

        # Calcular los años y meses de experiencia
        anios_completos = anio_actual - anio_inicio
        meses_completos = mes_actual - mes_inicio

        if mes_actual < mes_inicio:
            anios_completos -= 1
            meses_completos = 12 - abs(mes_actual - mes_inicio)

        # Calcular la fracción de año con los meses completos
        fraccion_anio = anios_completos + meses_completos / 12.0

        return fraccion_anio
