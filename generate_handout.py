#!/usr/bin/env python3
"""Generate a 2-page A4 handout PDF for ASPIRE Workshop 2026."""

from fpdf import FPDF

# ── Colours ──────────────────────────────────────────────────────────────
NAVY = (21, 32, 43)
DARK_BLUE = (30, 55, 90)
MID_BLUE = (55, 90, 140)
ACCENT = (70, 130, 180)       # steel-blue accent
WHITE = (255, 255, 255)
LIGHT_BG = (240, 244, 248)
TEXT_DARK = (33, 37, 41)
TEXT_MID = (80, 80, 80)
SESSION_BG = (232, 240, 248)
BREAK_BG = (245, 245, 240)


class HandoutPDF(FPDF):
    """Custom A4 PDF with helper drawing methods."""

    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=False)

    # ── tiny helpers ─────────────────────────────────────────────────
    def _set(self, r, g, b, *, fill=False, draw=False, text=False):
        if fill:
            self.set_fill_color(r, g, b)
        if draw:
            self.set_draw_color(r, g, b)
        if text:
            self.set_text_color(r, g, b)

    def _text_color(self, rgb):
        self.set_text_color(*rgb)

    def section_heading(self, title, y=None):
        if y is not None:
            self.set_y(y)
        self.set_font("Helvetica", "B", 10)
        self._text_color(NAVY)
        self._set(*NAVY, draw=True)
        x = self.l_margin
        w = self.epw
        top = self.get_y()
        self.set_x(x)
        self.cell(w, 5.5, f"  {title}", border=0, ln=1)
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.6)
        self.line(x, top + 5.8, x + w, top + 5.8)
        self.set_line_width(0.2)
        self.ln(1.5)


def build_page1(pdf: HandoutPDF):
    """Front page – conference info."""
    pdf.add_page()
    pw = pdf.epw  # effective page width
    lm = pdf.l_margin

    # ── Header banner ────────────────────────────────────────────────
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, 210, 38, "F")
    pdf.set_font("Helvetica", "B", 18)
    pdf._text_color(WHITE)
    pdf.set_y(7)
    pdf.cell(0, 8, "ASPIRE Workshop 2026", align="C", ln=1)
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(0, 5, "Establishment of an International Collaborative Research Network", align="C", ln=1)
    pdf.cell(0, 4, "on Human and Spatial Augmentation", align="C", ln=1)
    pdf.set_font("Helvetica", "B", 9)
    pdf._text_color((200, 220, 240))
    pdf.cell(0, 5.5, "March 12-14, 2026  |  Karuizawa Prince Hotel West  |  Nagano, Japan", align="C", ln=1)

    # ── Key Information ──────────────────────────────────────────────
    pdf.set_y(42)
    pdf.section_heading("Key Information")

    info_items = [
        ("Venue", 'Karuizawa Prince Hotel West, International Convention Hall "Asama"'),
        ("Transport", "Complimentary charter bus: Science Tokyo (Ookayama) <-> Karuizawa Prince Hotel"),
        ("Format", "15-min presentation + 5-min Q&A for postdocs and students"),
        ("Accommodation", "All participants stay at Karuizawa Prince Hotel West"),
        ("", "  * Single Room: Y64,300 / 2 nights   * Twin Room: Y79,800 / 2 nights (Y39,900 pp)"),
        ("Attendance Fee", "Approx. Y16,000 (TBA) per person, incl. Night Session on Mar 13"),
        ("Language", "English"),
    ]

    pdf.set_font("Helvetica", "", 7.5)
    for label, value in info_items:
        x = lm
        pdf.set_x(x)
        if label:
            pdf.set_font("Helvetica", "B", 7.5)
            pdf._text_color(DARK_BLUE)
            pdf.cell(28, 4, label + ":", ln=0)
            pdf.set_font("Helvetica", "", 7.5)
            pdf._text_color(TEXT_DARK)
            pdf.cell(pw - 28, 4, value, ln=1)
        else:
            pdf.set_font("Helvetica", "", 7.5)
            pdf._text_color(TEXT_MID)
            pdf.cell(28, 4, "", ln=0)
            pdf.cell(pw - 28, 4, value, ln=1)

    # ── ASPIRE Project Members ───────────────────────────────────────
    pdf.ln(2)
    pdf.section_heading("ASPIRE Project Members")

    members = [
        ("Albrecht Schmidt", "Professor", "LMU Munich"),
        ("Barry Brown", "Professor", "University of Copenhagen"),
        ("Daisuke Iwai", "Professor", "Osaka University"),
        ("Erwin Wu", "Research Assoc. Prof.", "Institute of Science Tokyo"),
        ("Frank Steinicke", "Professor", "University of Hamburg"),
        ("Gordon Wetzstein", "Assoc. Professor", "Stanford University"),
        ("Hideaki Kuzuoka", "Professor", "The University of Tokyo"),
        ("Hideki Koike", "Professor", "Institute of Science Tokyo"),
        ("Kris Kitani", "Research Assoc. Prof.", "Carnegie Mellon University"),
        ("Mark Billinghurst", "Professor", "University of South Australia"),
        ("Shio Miyafuji", "Asst. Professor", "Institute of Science Tokyo"),
        ("Takuji Narumi", "Assoc. Professor", "The University of Tokyo"),
    ]

    _draw_member_table(pdf, members, lm, pw)

    # ── Invited Guests ───────────────────────────────────────────────
    pdf.ln(2)
    pdf.section_heading("Invited Guests")

    guests = [
        ("Shigeo Morishima", "Professor", "Waseda University"),
        ("Katsutoshi Masai", "Asst. Professor", "Kyushu University"),
        ("Yuta Itoh", "Assoc. Professor", "Institute of Science Tokyo"),
    ]

    _draw_member_table(pdf, guests, lm, pw)

    # ── Contact ──────────────────────────────────────────────────────
    pdf.ln(2)
    pdf.section_heading("Contact")
    pdf.set_font("Helvetica", "", 7.5)
    pdf._text_color(TEXT_DARK)
    pdf.set_x(lm)
    pdf.cell(0, 4, "Hideki Koike: koike@c.titech.ac.jp     |     Erwin Wu: wu.e.aa@m.titech.ac.jp", ln=1)

    # ── Footer ───────────────────────────────────────────────────────
    pdf.set_y(-12)
    pdf.set_font("Helvetica", "I", 6.5)
    pdf._text_color(TEXT_MID)
    pdf.cell(0, 4, "ASPIRE Workshop 2026  |  Hosted by Koike Lab, Institute of Science Tokyo  |  JST ASPIRE Funded", align="C")


def _draw_member_table(pdf: HandoutPDF, members, lm, pw):
    """Draw a compact 3-column member table."""
    col_name = 38
    col_pos = 38
    col_aff = pw - col_name - col_pos
    row_h = 4.2

    # header
    pdf.set_font("Helvetica", "B", 7)
    pdf._text_color(WHITE)
    pdf.set_fill_color(*DARK_BLUE)
    pdf.set_x(lm)
    pdf.cell(col_name, row_h, "  Name", border=0, fill=True)
    pdf.cell(col_pos, row_h, "  Position", border=0, fill=True)
    pdf.cell(col_aff, row_h, "  Affiliation", border=0, fill=True, ln=1)

    pdf.set_font("Helvetica", "", 7)
    for i, (name, pos, aff) in enumerate(members):
        if i % 2 == 0:
            pdf.set_fill_color(*LIGHT_BG)
            fill = True
        else:
            fill = False
        pdf._text_color(TEXT_DARK)
        pdf.set_x(lm)
        pdf.cell(col_name, row_h, f"  {name}", border=0, fill=fill)
        pdf._text_color(TEXT_MID)
        pdf.cell(col_pos, row_h, f"  {pos}", border=0, fill=fill)
        pdf.cell(col_aff, row_h, f"  {aff}", border=0, fill=fill, ln=1)


# ── Page 2 ────────────────────────────────────────────────────────────────
def build_page2(pdf: HandoutPDF):
    """Back page – full 3-day schedule."""
    pdf.add_page()
    pw = pdf.epw
    lm = pdf.l_margin

    # ── Header banner ────────────────────────────────────────────────
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, 210, 14, "F")
    pdf.set_font("Helvetica", "B", 12)
    pdf._text_color(WHITE)
    pdf.set_y(4)
    pdf.cell(0, 6, "Program Schedule", align="C", ln=1)

    pdf.set_y(17)

    # ── Day 1 ────────────────────────────────────────────────────────
    _day_heading(pdf, "Day 1  - Thursday, March 12")

    day1 = [
        ("09:30-13:00", "Travel",      "Charter bus: Science Tokyo -> Karuizawa Prince Hotel", ""),
        ("13:00-13:45", "Lunch",       "Welcome Lunch & Registration", ""),
        ("13:45-14:00", "Opening",     "Opening Remarks", "Hideki Koike (Institute of Science Tokyo)"),
    ]
    day1_s1 = [
        ("14:00-14:20", "Session 1", "Exploring the Social Function of AI in Workplace and Relational Communication", "Chiran Yang (U. of Tokyo)"),
        ("14:20-14:40", "Session 1", "Designing for Sensory Experiences", "Tor Salve Dalsgaard (U. of Copenhagen)"),
        ("14:40-15:00", "Session 1", "Toward Cross-Agent 4D Interaction Generation", "Yichen Peng (Science Tokyo)"),
        ("15:00-15:20", "Session 1", "Comparing Partially-Stabilized and Skeletal Reference Frames for Intuitive Hand Guidance", "Takashige Suzuki (U. of Tokyo)"),
    ]
    day1_break = [("15:20-15:35", "Break", "Coffee Break", "")]
    day1_s2 = [
        ("15:35-15:55", "Session 2", "Effects of Agents and Avatars on Human Memory", "Takato Mizuho (U. of Tokyo)"),
        ("15:55-16:15", "Session 2", "A Progressive Training Method for Sports Skill Acquisition", "Chen-Chieh Liao (Science Tokyo)"),
        ("16:15-16:35", "Session 2", "Human-Centered XR for Time-Critical Flood Crisis Management", "Solmaz Goodarzi (U. of Hamburg)"),
        ("16:35-16:55", "Session 2", "Exploring Thermal Contact Potentials for Hand-Object Interaction Refinement", "Kohei Miura (Osaka U.)"),
    ]

    _schedule_rows(pdf, day1, lm, pw, is_meta=True)
    _schedule_rows(pdf, day1_s1, lm, pw)
    _schedule_rows(pdf, day1_break, lm, pw, is_meta=True)
    _schedule_rows(pdf, day1_s2, lm, pw)

    # ── Day 2 ────────────────────────────────────────────────────────
    pdf.ln(1.5)
    _day_heading(pdf, "Day 2  - Friday, March 13")

    day2_pre = [
        ("-14:00",      "Free Time",  "Individual Discussions & Collaboration Planning", ""),
        ("14:00-14:30", "Keynote",    "Keynote Speech", "Kris Kitani (Carnegie Mellon University)"),
    ]
    day2_s3 = [
        ("14:30-14:50", "Session 3", "Toward Intelligent Digital Twins: Perception Generation and Applications", "Qi Feng (Waseda U.)"),
        ("14:50-15:10", "Session 3", "From Shared Attention to Human-AI Collaboration", "Jesse Grootjen (LMU Munich)"),
        ("15:10-15:30", "Session 3", "Attention Guidance Using Saccade-Aware Cues", "Masahiro Nara (Science Tokyo)"),
    ]
    day2_break = [("15:30-16:00", "Break", "Coffee Break", "")]
    day2_s4 = [
        ("16:00-16:20", "Session 4", "Human-Robot Collaboration Design Space for Critical Large Scale Infrastructures", "Xinyu Chen (U. of Hamburg)"),
        ("16:20-16:40", "Session 4", "Track Understand and Augment Human States for Motor Skill Acquisition", "Ruofan Liu (Science Tokyo)"),
        ("16:40-17:00", "Session 4", "A Ski Coaching System Using Insole Sensors and Multimodal Large Language Models", "Toshihiro Hirano (Science Tokyo)"),
        ("17:00-17:20", "Session 4", "Target Image Adaptation in Projection Mapping Using Learnable Contrast and Brightness", "Thanapong Sommart (Osaka U.)"),
    ]
    day2_post = [
        ("17:20-17:30", "Closing",    "Day 2 Closing", ""),
        ("17:30-18:00", "Free Time",  "Break & Free Time", ""),
        ("18:00-21:00", "Evening",    "Free Discussion & Networking Dinner", ""),
    ]

    _schedule_rows(pdf, day2_pre, lm, pw, is_meta=True)
    _schedule_rows(pdf, day2_s3, lm, pw)
    _schedule_rows(pdf, day2_break, lm, pw, is_meta=True)
    _schedule_rows(pdf, day2_s4, lm, pw)
    _schedule_rows(pdf, day2_post, lm, pw, is_meta=True)

    # ── Day 3 ────────────────────────────────────────────────────────
    pdf.ln(1.5)
    _day_heading(pdf, "Day 3  - Saturday, March 14")

    day3_pre = [("09:00-09:10", "Opening", "Day 3 Opening", "")]
    day3_s5 = [
        ("09:10-09:30", "Session 5", "Contact4D: A Video Dataset for Whole-Body Human Motion and Finger Contact in Dexterous Operations", "Jyun-ting Song (CMU)"),
        ("09:30-09:50", "Session 5", "Toward Embodied AI that Promotes Trust Between Visually Impaired and Sighted Individuals", "Sotaro Yokoi (U. of Tokyo)"),
        ("09:50-10:10", "Session 5", "Humanity-centered Augmentation", "David Steeven Villa Salazar (LMU Munich)"),
        ("10:10-10:30", "Session 5", "Displaying Different Images Based on Gaze Movement Directions Using High-Speed Projection", "Ryusuke Miyazaki (Science Tokyo)"),
    ]
    day3_break = [("10:30-10:45", "Break", "Coffee Break", "")]
    day3_s6 = [
        ("10:45-11:05", "Session 6", "Enhancing Personalized Vision Through AR and Metaverse", "Yuichi Hiroi (Cluster Metaverse Lab)"),
        ("11:05-11:25", "Session 6", "Shadowless Projection Mapping with Large-Format Fresnel Lens", "Hiroki Kusuyama (Osaka U.)"),
        ("11:25-11:45", "Session 6", "Enhancing Material Appearance in Projection Mapping", "Masaki Takeuchi (Osaka U.)"),
        ("11:45-12:05", "Session 6", "Dependency-aware Non Linear Task Guidance in Augmented Reality", "Bowen Yuan (U. of South Australia)"),
    ]
    day3_post = [
        ("12:05-12:15", "Closing",  "Closing Remarks & Group Photo", ""),
        ("12:15-13:00", "Lunch",    "Farewell Lunch", ""),
        ("13:30-",      "Travel",   "Charter bus returns to Tokyo", ""),
    ]

    _schedule_rows(pdf, day3_pre, lm, pw, is_meta=True)
    _schedule_rows(pdf, day3_s5, lm, pw)
    _schedule_rows(pdf, day3_break, lm, pw, is_meta=True)
    _schedule_rows(pdf, day3_s6, lm, pw)
    _schedule_rows(pdf, day3_post, lm, pw, is_meta=True)

    # ── Footer ───────────────────────────────────────────────────────
    pdf.set_y(-8)
    pdf.set_font("Helvetica", "I", 6)
    pdf._text_color(TEXT_MID)
    pdf.cell(0, 4, "ASPIRE Workshop 2026  |  Karuizawa Prince Hotel West  |  JST ASPIRE Funded", align="C")


# ── Schedule drawing helpers ──────────────────────────────────────────────

def _day_heading(pdf: HandoutPDF, title: str):
    pdf.set_font("Helvetica", "B", 8.5)
    pdf._text_color(WHITE)
    pdf.set_fill_color(*DARK_BLUE)
    pdf.set_x(pdf.l_margin)
    pdf.cell(pdf.epw, 4.8, f"  {title}", fill=True, ln=1)
    pdf.ln(0.5)


ROW_H = 3.6
COL_TIME = 20
COL_BADGE = 15


def _schedule_rows(pdf: HandoutPDF, rows, lm, pw, *, is_meta=False):
    col_detail = pw - COL_TIME - COL_BADGE
    for time_str, badge, title, speaker in rows:
        y_start = pdf.get_y()

        # Determine how much width is left for the title + speaker
        title_w = col_detail
        if speaker:
            # We'll truncate long titles to keep it on one line
            full = f"{title}"
        else:
            full = title

        # Check if we need to wrap the title
        pdf.set_font("Helvetica", "B" if not is_meta else "", 6.2)
        title_text_w = pdf.get_string_width(full)
        needs_wrap = title_text_w > (title_w - 2)

        row_h = ROW_H
        if needs_wrap and not is_meta:
            row_h = ROW_H * 1.55  # a bit taller for wrapped rows

        # Background fill for alternating look
        if is_meta:
            pdf.set_fill_color(*BREAK_BG)
        else:
            pdf.set_fill_color(*SESSION_BG)

        pdf.set_x(lm)
        pdf.rect(lm, y_start, pw, row_h, "F")

        # Time column
        pdf.set_font("Helvetica", "", 5.8)
        pdf._text_color(TEXT_MID)
        pdf.set_xy(lm, y_start)
        pdf.cell(COL_TIME, row_h, f" {time_str}", ln=0)

        # Badge column
        pdf.set_font("Helvetica", "B", 5.5)
        if "Session" in badge:
            pdf._text_color(DARK_BLUE)
        elif badge == "Keynote":
            pdf._text_color((160, 60, 20))
        else:
            pdf._text_color(TEXT_MID)
        pdf.cell(COL_BADGE, row_h, badge, ln=0)

        # Title + speaker
        x_title = lm + COL_TIME + COL_BADGE
        pdf.set_xy(x_title, y_start)

        if is_meta:
            pdf.set_font("Helvetica", "", 6.2)
            pdf._text_color(TEXT_DARK)
            pdf.cell(title_w, row_h, title, ln=1)
        else:
            pdf.set_font("Helvetica", "B", 6.2)
            pdf._text_color(TEXT_DARK)
            if needs_wrap:
                # Multi-line: title on first line, speaker on second
                pdf.cell(title_w, ROW_H, full, ln=2)
                if speaker:
                    pdf.set_x(x_title)
                    pdf.set_font("Helvetica", "I", 5.8)
                    pdf._text_color(MID_BLUE)
                    pdf.cell(title_w, ROW_H * 0.55, speaker, ln=1)
            else:
                # Single line: title — speaker
                pdf.cell(title_w, row_h, full, ln=0)
                if speaker:
                    # overlay speaker after title
                    spk_x = x_title + pdf.get_string_width(full) + 2
                    if spk_x + pdf.get_string_width(speaker) < lm + pw:
                        pdf.set_xy(spk_x, y_start)
                        pdf.set_font("Helvetica", "I", 5.8)
                        pdf._text_color(MID_BLUE)
                        pdf.cell(0, row_h, speaker, ln=1)
                    else:
                        pdf.ln(0)

        pdf.set_y(y_start + row_h + 0.3)


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    pdf = HandoutPDF()
    pdf.set_margins(8, 8, 8)

    build_page1(pdf)
    build_page2(pdf)

    pdf.output("handout.pdf")
    print("Created handout.pdf (2 pages)")


if __name__ == "__main__":
    main()
