import qrcode
import tkinter as tk
from tkinter import messagebox

def generate_qr_code():
    # Получение данных из полей ввода
    name = name_entry.get()
    position = position_entry.get()
    company = company_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    phone = phone_entry.get()
    telegram = telegram_entry.get()

    # Разделение имени и фамилии
    name_parts = name.split()
    first_name = name_parts[0]
    last_name = name_parts[1] if len(name_parts) > 1 else ""

    # Формирование текста для QR-кода
    qr_text = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name}\nORG:{company}\nTITLE:{position}\nEMAIL:{email}\nURL:{website}\nTEL:{phone}\nNOTE:Telegram: {telegram}\nEND:VCARD"

    # Создание QR-кода
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_text)
    qr.make(fit=True)

    # Сохранение QR-кода в файл
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{last_name}_{first_name}_qr_code.png")

    # Очистка полей ввода
    name_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    company_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    website_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    telegram_entry.delete(0, tk.END)

    # Вывод сообщения об успешном сохранении
    messagebox.showinfo("Успех", "QR-код успешно сохранен")

def on_entry_right_click(entry):
    def on_right_click(event):
        context_menu = tk.Menu(root, tearoff=0)
        context_menu.add_command(label="Вставить", command=lambda: entry.event_generate('<<Paste>>'))
        context_menu.tk_popup(event.x_root, event.y_root)
    return on_right_click

# Создание главного окна
root = tk.Tk()
root.title("Генератор QR-кодов")

# Создание и размещение элементов управления
name_label = tk.Label(root, text="Имя и фамилия:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
name_entry.bind("<Button-3>", on_entry_right_click(name_entry))

company_label = tk.Label(root, text="Название компании:")
company_label.grid(row=2, column=0)
company_entry = tk.Entry(root)
company_entry.grid(row=2, column=1)
company_entry.bind("<Button-3>", on_entry_right_click(company_entry))

position_label = tk.Label(root, text="Должность:")
position_label.grid(row=1, column=0)
position_entry = tk.Entry(root)
position_entry.grid(row=1, column=1)
position_entry.bind("<Button-3>", on_entry_right_click(position_entry))

email_label = tk.Label(root, text="Email:")
email_label.grid(row=3, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1)
email_entry.bind("<Button-3>", on_entry_right_click(email_entry))

website_label = tk.Label(root, text="Веб-сайт:")
website_label.grid(row=4, column=0)
website_entry = tk.Entry(root)
website_entry.grid(row=4, column=1)
website_entry.bind("<Button-3>", on_entry_right_click(website_entry))

phone_label = tk.Label(root, text="Телефон:")
phone_label.grid(row=5, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=5, column=1)
phone_entry.bind("<Button-3>", on_entry_right_click(phone_entry))

telegram_label = tk.Label(root, text="Telegram:")
telegram_label.grid(row=6, column=0)
telegram_entry = tk.Entry(root)
telegram_entry.grid(row=6, column=1)
telegram_entry.bind("<Button-3>", on_entry_right_click(telegram_entry))

generate_button = tk.Button(root, text="Сгенерировать QR-код", command=generate_qr_code)
generate_button.grid(row=7, columnspan=2)
# Запуск главного цикла обработки событий
root.mainloop()