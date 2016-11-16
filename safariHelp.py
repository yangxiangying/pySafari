from terminaltables import AsciiTable, DoubleTable, SingleTable
from colorclass import Color, Windows

def help():
    table_data = [
        [Color('{autoyellow}ref{/autoyellow}'), '快參', '例子'],
        [Color('{autoblue}source{/autoblue}'), '源碼', 'safari source'],
        [Color('{autoblue}regex{/autoblue}'), '正則',
         'safari regex "[A-Z]+\-[0-9]{3}"'],
        [Color('{autoblue}history{/autoblue}'), '歷史', 'safari history'],
        [Color('{autoblue}favorite{/autoblue}'), '收藏', 'safari favorite'],
        [Color('{autoblue}net{/autoblue}'), '網路', 'safari net'],
        [Color('{autoblue}moveto{/autoblue}'), '移動', 'safari move'],
        [Color('{autoblue}plugin{/autoblue}'), '插件', 'safari plugin'],
        [Color('{autoblue}new{/autoblue}'), '重置(慎)', 'safari new'],
        [Color('{autoblue}edit{/autoblue}'), '編輯(開發)', 'safari edit'],
    ]
    table_instance = SingleTable(table_data, '開發')
    table_instance.inner_heading_row_border = False
    table_instance.inner_row_border = True


    return table_instance.table
