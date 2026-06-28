import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------
# PHYSICS LOGIC & CALCULATION FUNCTION
# ---------------------------------------------------------
def calculate_dose():
    try:
        # 1. Retrieve values from the user interface
        ctdi_vol = float(entry_ctdi.get())
        scan_length = float(entry_length.get())
        region = combo_region.get()
        
        # 2. Basic CT Physics Formula: DLP = CTDIvol * Scan Length
        # Unit: mGy * cm = mGy-cm
        dlp = ctdi_vol * scan_length
        
        # 3. Define Standard ICRP k-factors (Conversion Coefficients)
        # These constants approximate Effective Dose based on body region
        k_factors = {
            "Head": 0.0021,
            "Chest": 0.0140,
            "Abdomen/Pelvis": 0.0150
        }
        
        k_factor = k_factors[region]
        
        # 4. Advanced Physics Formula: Effective Dose = DLP * k-factor
        # Unit: mGy-cm * (mSv / (mGy-cm)) = mSv
        effective_dose = dlp * k_factor
        
        # 5. Update the UI labels with results (rounded to 3 decimal places)
        label_dlp_result.config(text=f"{dlp:.2f} mGy·cm", fg="#1e3a8a")
        label_ed_result.config(text=f"{effective_dose:.3f} mSv", fg="#0d9488")
        
    except ValueError:
        # Error handling if the user inputs text instead of numbers
        messagebox.showerror("Input Error", "Please enter valid numerical values for CTDIvol and Scan Length.")

# ---------------------------------------------------------
# USER INTERFACE SETUP (Tkinter)
# ---------------------------------------------------------
# Initialize main window
root = tk.Tk()
root.title("CT Dose Index & DLP Estimator")
root.geometry("450x520")
root.configure(bg="#f3f4f6") # Clinical light-gray background

# Title Banner
title_label = tk.Label(root, text="CT Dose & Risk Estimator", font=("Helvetica", 16, "bold"), bg="#1e3a8a", fg="white", pady=10)
title_label.pack(fill=tk.X)

# Subtitle/Department
dept_label = tk.Label(root, text="Medical Physics Department Tool", font=("Helvetica", 9, "italic"), bg="#f3f4f6", fg="#4b5563")
dept_label.pack(pady=5)

# Frame for Inputs
input_frame = tk.Frame(root, bg="#f3f4f6", padx=20, pady=10)
input_frame.pack(fill=tk.X)

# Input 1: CTDIvol
tk.Label(input_frame, text="CTDIvol (mGy):", font=("Helvetica", 11, "bold"), bg="#f3f4f6", fg="#1f2937").grid(row=0, column=0, sticky="w", pady=5)
entry_ctdi = tk.Entry(input_frame, font=("Helvetica", 11), width=15)
entry_ctdi.grid(row=0, column=1, pady=5, padx=10)

# Input 2: Scan Length
tk.Label(input_frame, text="Scan Length (cm):", font=("Helvetica", 11, "bold"), bg="#f3f4f6", fg="#1f2937").grid(row=1, column=0, sticky="w", pady=5)
entry_length = tk.Entry(input_frame, font=("Helvetica", 11), width=15)
entry_length.grid(row=1, column=1, pady=5, padx=10)

# Input 3: Region Dropdown
tk.Label(input_frame, text="Scan Region:", font=("Helvetica", 11, "bold"), bg="#f3f4f6", fg="#1f2937").grid(row=2, column=0, sticky="w", pady=5)
combo_region = ttk.Combobox(input_frame, font=("Helvetica", 11), values=["Head", "Chest", "Abdomen/Pelvis"], state="readonly", width=13)
combo_region.current(1) # Default to Chest
combo_region.grid(row=2, column=1, pady=5, padx=10)

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate Patient Dose", font=("Helvetica", 12, "bold"), bg="#0d9488", fg="white", activebackground="#0f766e", activeforeground="white", bd=0, padx=20, pady=8, command=calculate_dose)
btn_calculate.pack(pady=15)

# Separator Line
divider = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN, bg="#e5e7eb")
divider.pack(fill=tk.X, padx=20, pady=5)

# Results Display Frame
results_frame = tk.Frame(root, bg="#f3f4f6", padx=20, pady=10)
results_frame.pack(fill=tk.X)

# DLP Output
tk.Label(results_frame, text="Dose Length Product (DLP):", font=("Helvetica", 11), bg="#f3f4f6", fg="#4b5563").grid(row=0, column=0, sticky="w", pady=5)
label_dlp_result = tk.Label(results_frame, text="-- mGy·cm", font=("Helvetica", 12, "bold"), bg="#f3f4f6", fg="#9ca3af")
label_dlp_result.grid(row=0, column=1, sticky="w", padx=10)

# Effective Dose Output
tk.Label(results_frame, text="Estimated Effective Dose:", font=("Helvetica", 11), bg="#f3f4f6", fg="#4b5563").grid(row=1, column=0, sticky="w", pady=5)
label_ed_result = tk.Label(results_frame, text="-- mSv", font=("Helvetica", 14, "bold"), bg="#f3f4f6", fg="#9ca3af")
label_ed_result.grid(row=1, column=1, sticky="w", padx=10)

# Clinical Disclaimer Footer
disclaimer_text = "Disclaimer: This software is an educational prototype mapping ICRP conversion coefficients. It is not a calibrated tool for direct clinical diagnostics or formal safety logs."
lbl_disclaimer = tk.Label(root, text=disclaimer_text, font=("Helvetica", 8), bg="#f3f4f6", fg="#9ca3af", wraplength=400, justify="center")
lbl_disclaimer.pack(side=tk.BOTTOM, pady=15)

# Start the application loop
root.mainloop()