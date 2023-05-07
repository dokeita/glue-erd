import boto3
import click

glue = boto3.client("glue")

@click.command()
@click.option('--db_name', '-d', required=True, help='database name')
@click.option('-table_name', '-t', default='', help='table name')
@click.option('-out_dir', '-o', default='.', help='output directory. default: current directory')
def main(db_name, table_name, out_dir):

    table_names = []
    if table_name:
        table_names.append(table_name)
    else:
        table_names = get_tables(db_name)

    table_erds = []
    table_erds.append(f'```mermaid\n')
    table_erds.append(f'erDiagram\n')
    for item in table_names:
        table_erds = table_erds + get_table_erd(db_name, item)
    table_erds.append(f'```\n')


    output(db_name, table_erds, out_dir, table_name)


def get_table_erd(db_name, table_name):

    table = glue.get_table(DatabaseName=db_name, Name=table_name)

    name = table.get('Table').get('Name')
    columns = table.get('Table').get('StorageDescriptor').get('Columns')

    lines = []
    lines.append(f'    {name} {{\n')
    for item in columns:
        lines.append(f'        {item.get("Type")} {item.get("Name")}\n')
    lines.append(f'    }}\n')

    return lines

def output(db_name, lines, out_dir, table_name=None):
    
    filename = f'{out_dir}/{db_name}{ "_"+table_name if table_name else ""}.md'
    with open(filename, 'w', encoding="utf-8", newline='') as f:
        f.writelines(lines)


def get_tables(db_name):
    tables = []
    response = glue.get_tables(DatabaseName=db_name)
    if response:
        for table in response.get('TableList'):
            tables.append(table.get('Name'))

    while 'NextToken' in response:
        response = glue.get_tables(DatabaseNam=db_name, NextToken=response.get('NextToken'))
        if response:
            for table in response.get('TableList'):
                tables.append(table.get('Name'))

    return tables

if __name__ == '__main__':
    main()