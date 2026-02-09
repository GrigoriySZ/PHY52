import sqlite3


def print_database_clean(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        for table_name_tuple in tables:
            table_name = table_name_tuple[0]
            print(f"\n>>> ТАБЛИЦА: {table_name}")

            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

            headers = [description[0] for description in cursor.description]

            if not rows:
                print("   (Таблица пуста)")
                continue
            col_widths = []
            for i, header in enumerate(headers):
                max_len = len(str(header))
                for row in rows:
                    val_len = len(str(row[i] if row[i] is not None else "NULL"))
                    if val_len > max_len:
                        max_len = val_len
                col_widths.append(max_len)

            row_format = " | ".join(["{:<" + str(w) + "}" for w in col_widths])
            separator = "-+-".join(["-" * w for w in col_widths])

            print(row_format.format(*headers))
            print(separator)
            for row in rows:
                display_row = [str(item) if item is not None else "NULL" for item in row]
                print(row_format.format(*display_row))

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    print_database_clean('company.db')