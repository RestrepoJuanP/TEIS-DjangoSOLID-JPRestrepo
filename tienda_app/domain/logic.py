from decimal import Decimal, ROUND_HALF_UP


class CalculadorImpuestos:
    """
    S: Responsabilidad única - Solo calcula impuestos.
    O: Abierto a extensión - Podríamos heredar para diferentes países.
    """
    IVA = Decimal("1.19")

    @staticmethod
    def obtener_total_con_iva(precio_base) -> Decimal:
        total = Decimal(str(precio_base)) * CalculadorImpuestos.IVA
        return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)