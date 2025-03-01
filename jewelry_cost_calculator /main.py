# main.py
from metal_price_api import get_metal_price
from calculator import calculate_metal_cost
from gemstone_calculator import calculate_gemstone_cost
from tax_calculator import calculate_tax
from save_quote import save_quote, share_quote
import tkinter as tk
from tkinter import ttk, messagebox

def calculate_cost():
    metal_type = metal_var.get()
    if not metal_type:
        messagebox.showerror("Error", "Please select a metal type.")
        return
    
    try:
        weight = float(weight_entry.get())
        purity = float(purity_entry.get())
        making_charges_percent = float(making_charges_entry.get())
        tax_rate = float(tax_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        return
    
    metal_price_per_gram = get_metal_price(metal_type)  # Fetch price dynamically
    metal_cost = calculate_metal_cost(weight, purity, metal_price_per_gram, metal_type)
    making_charges = metal_cost * (making_charges_percent / 100)
    subtotal = metal_cost + making_charges
    
    gemstone_cost = 0
    if gemstone_var.get():
        try:
            carat_weight = float(carat_weight_entry.get())
            quality_factor = float(quality_factor_entry.get())
            gemstone_cost = calculate_gemstone_cost(gemstone_type_entry.get(), carat_weight, quality_factor)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid gemstone details.")
            return
        subtotal += gemstone_cost
    
    tax = calculate_tax(subtotal, tax_rate)
    total_cost = subtotal + tax
    
    result_label.config(text=f"Total Cost: INR {total_cost:.2f}")
    return {
        "metal_type": metal_type,
        "metal_cost": metal_cost,
        "making_charges": making_charges,
        "gemstone_cost": gemstone_cost,
        "subtotal": subtotal,
        "tax": tax,
        "total_cost": total_cost,
    }

def save_quote():
    quote = calculate_cost()
    if quote:
        with open("jewelry_quote.txt", "w") as file:
            file.write(str(quote))
        messagebox.showinfo("Saved", "Quote saved successfully.")

def share_quote():
    quote = calculate_cost()
    if quote:
        messagebox.showinfo("Shared", "Quote shared successfully!")

if __name__ == "__main__":
    
    # UI Setup
    root = tk.Tk()
    root.title("Jewelry Cost Calculator")
    root.geometry("400x500")

    ttk.Label(root, text="Metal Type:").pack()
    metal_var = tk.StringVar()
    metal_dropdown = ttk.Combobox(root, textvariable=metal_var, values=["gold", "silver"])
    metal_dropdown.pack()

    ttk.Label(root, text="Weight (grams):").pack()
    weight_entry = ttk.Entry(root)
    weight_entry.pack()

    ttk.Label(root, text="Purity:").pack()
    purity_entry = ttk.Entry(root)
    purity_entry.pack()

    ttk.Label(root, text="Making Charges (%):").pack()
    making_charges_entry = ttk.Entry(root)
    making_charges_entry.pack()

    ttk.Label(root, text="Tax Rate (%):").pack()
    tax_entry = ttk.Entry(root)
    tax_entry.pack()

    gemstone_var = tk.BooleanVar()
    gemstone_check = ttk.Checkbutton(root, text="Include Gemstones", variable=gemstone_var)
    gemstone_check.pack()

    ttk.Label(root, text="Gemstone Type:").pack()
    gemstone_type_entry = ttk.Entry(root)
    gemstone_type_entry.pack()

    ttk.Label(root, text="Carat Weight:").pack()
    carat_weight_entry = ttk.Entry(root)
    carat_weight_entry.pack()

    ttk.Label(root, text="Quality Factor:").pack()
    quality_factor_entry = ttk.Entry(root)
    quality_factor_entry.pack()

    calculate_button = ttk.Button(root, text="Calculate", command=calculate_cost)
    calculate_button.pack()

    save_button = ttk.Button(root, text="Save Quote", command=save_quote)
    save_button.pack()

    share_button = ttk.Button(root, text="Share Quote", command=share_quote)
    share_button.pack()

    result_label = ttk.Label(root, text="")
    result_label.pack()

    root.mainloop()