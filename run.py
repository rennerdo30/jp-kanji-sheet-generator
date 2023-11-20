from jisho_api.kanji import Kanji
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import CIDFont, findCMapFile, UnicodeCIDFont


def generate_kanji_sheet(kanji, filename=f'kanji_sheet.pdf', grid_size=10, box_size=60):

    filename = f"{kanji.kanji}_sheet.pdf"

    meanings = kanji.main_meanings
    meanings_str = ""
    for meaning in meanings:
        meanings_str = meanings_str + " | " + meaning

    readings = kanji.main_readings
    readings_on_str = "On'yomi: "
    if readings.on:
        for reading in readings.on:
            readings_on_str = readings_on_str + " | " + reading

    readings_kun_str = "Kun'yomi: "
    if readings.kun:
        for reading in readings.kun:
            readings_kun_str = readings_kun_str + " | " + reading

    c = canvas.Canvas(filename, pagesize=letter)

    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

    font_size = 32

    font_name = "HeiseiMin-W3"
    c.setFont(font_name, font_size)

    text_x = 8
    c.drawString(text_x, 760, f"{kanji.kanji} {meanings_str}")
    c.drawString(text_x, 725, f"{readings_on_str}")
    c.drawString(text_x, 690, f"{readings_kun_str}")

    for i in range(grid_size):
        for j in range(grid_size):
            x1 = text_x + i * box_size
            y1 = 610 - j * box_size
            x2 = x1 + box_size
            y2 = y1 - box_size
            c.rect(x1, y1, box_size, box_size)

    c.save()

if __name__ == "__main__":
    with open('input.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
            kanji_character = line.strip()

            r = Kanji.request(kanji_character)
            if r:
                print(r.data)
                print(r.data.main_meanings)
                print(r.data.main_readings)
                generate_kanji_sheet(r.data)
