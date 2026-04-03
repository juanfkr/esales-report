from weasyprint import HTML, CSS
from datetime import datetime
import json

class ReportGenerator:
    def __init__(self, metrics: dict):
        self.metrics = metrics

    def generate_pdf(self, output_path: str) -> None:
        """Gera relatório PDF com base nas métricas"""
        html_content = self._generate_html()
        HTML(string=html_content).write_pdf(output_path)

    def _generate_html(self) -> str:
        """Cria HTML com estilo e dados das métricas"""
        m = self.metrics
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; color: #333; }}
                h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
                h2 {{ color: #34495e; margin-top: 30px; }}
                .metric {{ display: inline-block; width: 23%; margin: 1%; padding: 15px; background: #ecf0f1; border-radius: 5px; text-align: center; }}
                .metric-value {{ font-size: 24px; font-weight: bold; color: #3498db; }}
                .metric-label {{ font-size: 12px; color: #7f8c8d; margin-top: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
                th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #bdc3c7; }}
                th {{ background: #3498db; color: white; }}
                tr:nth-child(even) {{ background: #ecf0f1; }}
                .footer {{ margin-top: 40px; font-size: 10px; color: #95a5a6; text-align: center; }}
            </style>
        </head>
        <body>
            <h1>E-Sales Report</h1>
            <p><strong>Período:</strong> {m['period']}</p>
            
            <div class="metric">
                <div class="metric-value">{m['total_orders']}</div>
                <div class="metric-label">Total de Pedidos</div>
            </div>
            <div class="metric">
                <div class="metric-value">R$ {m['total_revenue']:,.2f}</div>
                <div class="metric-label">Receita Total</div>
            </div>
            <div class="metric">
                <div class="metric-value">R$ {m['average_order_value']:,.2f}</div>
                <div class="metric-label">Ticket Médio</div>
            </div>
            <div class="metric">
                <div class="metric-value">{m['delivery_rate']:.1f}%</div>
                <div class="metric-label">Taxa de Entrega</div>
            </div>

            <h2>Status dos Pedidos</h2>
            <table>
                <tr><th>Status</th><th>Quantidade</th></tr>
                <tr><td>Entregues</td><td>{m['delivered_orders']}</td></tr>
                <tr><td>Cancelados</td><td>{m['cancelled_orders']}</td></tr>
                <tr><td>Devolvidos</td><td>{m['returned_orders']}</td></tr>
            </table>

            <h2>Top 5 Categorias</h2>
            <table>
                <tr><th>Categoria</th><th>Pedidos</th></tr>
                {self._render_table_rows(m['top_categories'])}
            </table>

            <h2>Top 5 Marcas</h2>
            <table>
                <tr><th>Marca</th><th>Pedidos</th></tr>
                {self._render_table_rows(m['top_brands'])}
            </table>

            <h2>Receita por País</h2>
            <table>
                <tr><th>País</th><th>Receita (R$)</th></tr>
                {self._render_revenue_rows(m['top_countries'])}
            </table>

            <h2>Receita por Método de Pagamento</h2>
            <table>
                <tr><th>Método</th><th>Receita (R$)</th></tr>
                {self._render_revenue_rows(m['revenue_by_payment'])}
            </table>

            <h2>Resumo Financeiro</h2>
            <table>
                <tr><th>Item</th><th>Valor (R$)</th></tr>
                <tr><td>Descontos</td><td>{m['total_discount']:,.2f}</td></tr>
                <tr><td>Impostos</td><td>{m['total_tax']:,.2f}</td></tr>
                <tr><td>Frete</td><td>{m['total_shipping']:,.2f}</td></tr>
            </table>

            <div class="footer">
                <p>Relatório gerado em {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}</p>
            </div>
        </body>
        </html>
        """
        return html

    def _render_table_rows(self, data: dict) -> str:
        """Renderiza linhas de tabela simples"""
        rows = ""
        for key, value in data.items():
            rows += f"<tr><td>{key}</td><td>{value}</td></tr>"
        return rows

    def _render_revenue_rows(self, data: dict) -> str:
        """Renderiza linhas de tabela com valores monetários"""
        rows = ""
        for key, value in data.items():
            rows += f"<tr><td>{key}</td><td>R$ {value:,.2f}</td></tr>"
        return rows