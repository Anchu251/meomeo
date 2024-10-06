import tkinter as tk
from tkinter import messagebox
import csv
import os

# Định nghĩa lớp Team
class Team:
    def __init__(self, fc, max_players):
        self.fc = fc
        self.players = []
        self.max_players = max_players

    def add_player(self, player_name):
        if len(self.players) < self.max_players:
            if player_name not in self.players:
                self.players.append(player_name)
                return True
        return False

# Định nghĩa lớp Set
class Set:
    def __init__(self, match_id, team1, team2, time, field):
        self.match_id = match_id
        self.teams = [team1, team2]
        self.time = time
        self.field = field
        self.score = None

    def record_result(self, score):
        self.score = score

# Tạo giao diện
class SportsManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý lịch thi đấu thể thao")
        self.root.geometry('500x500')
        self.teams = []  # Danh sách các đội
        self.matches = []  # Danh sách các trận đấu
        self.create_main_menu()

    def create_main_menu(self):
        # Xóa các widget cũ
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text="Chọn dịch vụ", font=('Arial', 18))
        label.pack(pady=20)

        add_button = tk.Button(self.root, text='Thêm cầu thủ', font=('Arial', 16), command=self.show_add_player_screen)
        add_button.pack(pady=10)

        fc_button = tk.Button(self.root, text='Thêm đội', font=('Arial', 16), command=self.show_add_team_screen)
        fc_button.pack(pady=10)

        set_button = tk.Button(self.root, text='Đặt kèo thi đấu', font=('Arial', 16), command=self.show_schedule_match_screen)
        set_button.pack(pady=10)

        view_button = tk.Button(self.root, text='Xem lịch thi đấu', font=('Arial', 16), command=self.show_match_schedule)
        view_button.pack(pady=10)

    def show_add_player_screen(self):
        # Xóa các widget cũ
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text="Thêm cầu thủ vào đội", font=('Arial', 18))
        label.pack(pady=20)

        tk.Label(self.root, text="Tên cầu thủ:").pack()
        player_name_entry = tk.Entry(self.root)
        player_name_entry.pack()

        tk.Label(self.root, text="Chọn đội:").pack()
        team_options = [team.fc for team in self.teams]  # Danh sách các đội có sẵn
        selected_team = tk.StringVar(self.root)
        if team_options:
            selected_team.set(team_options[0])  # Đặt đội đầu tiên làm mặc định
        team_dropdown = tk.OptionMenu(self.root, selected_team, *team_options)
        team_dropdown.pack()

        def add_player():
            player_name = player_name_entry.get()
            team_name = selected_team.get()

            for team in self.teams:
                if team.fc == team_name:
                    if team.add_player(player_name):
                        messagebox.showinfo("Thành công", f"Cầu thủ '{player_name}' đã được thêm vào đội '{team_name}'.")
                    else:
                        messagebox.showwarning("Thất bại", f"Đội '{team_name}' đã đạt số lượng cầu thủ tối đa hoặc cầu thủ đã tồn tại.")
                    break

        tk.Button(self.root, text="Thêm cầu thủ", command=add_player).pack(pady=10)
        tk.Button(self.root, text="Quay lại", command=self.create_main_menu).pack(pady=10)

    def show_add_team_screen(self):
        # Xóa các widget cũ
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text="Thêm đội bóng", font=('Arial', 18))
        label.pack(pady=20)

        tk.Label(self.root, text="Tên đội bóng:").pack()
        team_name_entry = tk.Entry(self.root)
        team_name_entry.pack()

        tk.Label(self.root, text="Số người tối đa:").pack()
        max_players_entry = tk.Entry(self.root)
        max_players_entry.pack()

        def add_team():
            team_name = team_name_entry.get()
            try:
                max_players = int(max_players_entry.get())
                new_team = Team(team_name, max_players)
                self.teams.append(new_team)
                messagebox.showinfo("Thành công", f"Đội bóng '{team_name}' đã được thêm với {max_players} người.")
            except ValueError:
                messagebox.showwarning("Lỗi", "Số người tối đa phải là số.")

        tk.Button(self.root, text="Thêm đội", command=add_team).pack(pady=10)
        tk.Button(self.root, text="Quay lại", command=self.create_main_menu).pack(pady=10)

    def show_schedule_match_screen(self):
        # Xóa các widget cũ
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text="Đặt kèo thi đấu", font=('Arial', 18))
        label.pack(pady=20)

        tk.Label(self.root, text="Thời gian thi đấu:").pack()
        time_entry = tk.Entry(self.root)
        time_entry.pack()

        tk.Label(self.root, text="Sân thi đấu (1 hoặc 2):").pack()
        field_entry = tk.Entry(self.root)
        field_entry.pack()

        tk.Label(self.root, text="Chọn đội 1:").pack()
        team_options = [team.fc for team in self.teams]  # Danh sách các đội
        selected_team1 = tk.StringVar(self.root)
        if team_options:
            selected_team1.set(team_options[0])  # Đặt đội đầu tiên làm mặc định
        team1_dropdown = tk.OptionMenu(self.root, selected_team1, *team_options)
        team1_dropdown.pack()

        tk.Label(self.root, text="Chọn đội 2:").pack()
        selected_team2 = tk.StringVar(self.root)
        if team_options:
            selected_team2.set(team_options[0])  # Đặt đội đầu tiên làm mặc định
        team2_dropdown = tk.OptionMenu(self.root, selected_team2, *team_options)
        team2_dropdown.pack()

        def schedule_match():
            time = time_entry.get()
            field = field_entry.get()
            team1_name = selected_team1.get()
            team2_name = selected_team2.get()

            team1 = None
            team2 = None
            for team in self.teams:
                if team.fc == team1_name:
                    team1 = team
                if team.fc == team2_name:
                    team2 = team

            if team1 and team2 and field in ['1', '2']:
                match_id = len(self.matches) + 1
                match = Set(f"Match-{match_id}", team1, team2, time, field)
                self.matches.append(match)
                self.save_match_to_csv(match)
                messagebox.showinfo("Thành công", f"Trận đấu giữa '{team1_name}' và '{team2_name}' đã được lên lịch.")
            else:
                messagebox.showwarning("Lỗi", "Vui lòng chọn thông tin hợp lệ.")

        tk.Button(self.root, text="Đặt lịch", command=schedule_match).pack(pady=10)
        tk.Button(self.root, text="Quay lại", command=self.create_main_menu).pack(pady=10)

    def save_match_to_csv(self, match):
        file_exists = os.path.isfile("match_schedule.csv")
        with open("match_schedule.csv", mode="a", newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Match ID", "Team 1", "Team 2", "Time", "Field"])
            writer.writerow([match.match_id, match.teams[0].fc, match.teams[1].fc, match.time, match.field])

    def show_match_schedule(self):
        # Xóa các widget cũ
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text="Danh sách lịch thi đấu", font=('Arial', 18))
        label.pack(pady=20)

        try:
            with open("match_schedule.csv", mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    match_info = f"Trận: {row[0]}, {row[1]} vs {row[2]}, Thời gian: {row[3]}, Sân: {row[4]}"
                    tk.Label(self.root, text=match_info).pack()
        except FileNotFoundError:
            tk.Label(self.root, text="Không có lịch thi đấu nào.").pack()

        tk.Button(self.root, text="Quay lại", command=self.create_main_menu).pack(pady=10)

# Tạo ứng dụng
root = tk.Tk()
app = SportsManagementApp(root)
root.mainloop()
