import datetime

from ..domain.interfaces import ProcesadorPago


class BancoNacionalProcesador(ProcesadorPago):
    """
    Implementación concreta de infraestructura.
    Simula un banco escribiendo en un log local.
    """

    def pagar(self, monto: float) -> bool:
        archivo_log = "pagos_locales_Juan_Pablo_Restrepo.log"

        with open(archivo_log, "a") as f:
            f.write(f"[{datetime.datetime.now()}] Transaccion exitosa por: ${monto}\n")
        return True