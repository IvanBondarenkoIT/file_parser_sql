import sqlparse
import pandas
import data_manager as dm


CSV_FILE_PATH = 'result_csv_file.csv'
NO_VALID_FILE_PATH = "not_valid_data.csv"
SQL_FILE_PATH = 'data.sql'


def read_sql_file(filename: str):
    sql_file = open(filename, 'r', encoding="utf8")
    sql_content = sql_file.read()
    parsed = sqlparse.parse(sql_content)

    for statement in parsed:
        tokens = statement.tokens
        for token in tokens:
            yield token

    sql_file.close()


def main():
    data_interpreter = dm.DataInterpreter()

    for record in read_sql_file(SQL_FILE_PATH):
        data_interpreter.add_data(record)

    df = pandas.DataFrame(data_interpreter.get_final_values)
    df.to_csv(CSV_FILE_PATH, index=False, header=False)

    df = pandas.DataFrame(data_interpreter.get_not_valid_data)
    df.to_csv(NO_VALID_FILE_PATH, index=False, header=False)


if __name__ == '__main__':
    main()

