import tkinter as tk
import requests

def get_location():
    ip_address = ip_entry.get()
    access_token = "YOUR TOKEN"


    url = f"https://ipinfo.io/{ip_address}/json?token={access_token}"
    response = requests.get(url)

    data = response.json()
    city = data.get("city", "Unknown")
    region = data.get("region", "Unknown")
    country = data.get("country", "Unknown")
    latitude, longitude = data.get("loc", "Unknown").split(",")
    zip_code = data.get("postal", "Unknown")
    area_code = data.get("phone", "Unknown")
    isp = data.get("org", "Unknown")
    hostname = data.get("hostname", "Unknown")
    os = data.get("os", "Unknown")
    services = data.get("services", "Unknown")
    malicious = data.get("threat", {}).get("is_threat", "Unknown")
    proxy = data.get("proxy", {}).get("proxy", "Unknown")

    mobile_url = f"https://ipinfo.io/{ip_address}/carrier?token={access_token}"
    mobile_response = requests.get(mobile_url)
    mobile_data = mobile_response.json()
    mcc = mobile_data.get("mcc", "Unknown")
    mnc = mobile_data.get("mnc", "Unknown")
    carrier = mobile_data.get("carrier", "Unknown")
    cc = mobile_data.get("cc", "Unknown")
    network = mobile_data.get("network", "Unknown")

    city_label.config(text=f"City: {city}")
    region_label.config(text=f"Region: {region}")
    country_label.config(text=f"Country: {country}")
    latitude_label.config(text=f"Latitude: {latitude}")
    longitude_label.config(text=f"Longitude: {longitude}")
    zip_code_label.config(text=f"Zip Code: {zip_code}")
    area_code_label.config(text=f"Area Code: {area_code}")
    isp_label.config(text=f"ISP: {isp}")
    hostname_label.config(text=f"Hostname: {hostname}")

root = tk.Tk()
root.title("IP Analysis")


root.geometry("600x500")
root.configure(bg="#2c3e50")


ip_label = tk.Label(root, text="Enter IP address:", font=("Arial", 16), fg="white", bg="#2c3e50")
ip_label.pack(pady=20)
ip_entry = tk.Entry(root, font=("Arial", 14))
ip_entry.pack(pady=10)


city_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
city_label.pack()
region_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
region_label.pack()
country_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
country_label.pack()
latitude_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
latitude_label.pack()
longitude_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
longitude_label.pack()
zip_code_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
zip_code_label.pack()
area_code_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
area_code_label.pack()
isp_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
isp_label.pack()
hostname_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
hostname_label.pack()


get_location_button = tk.Button(root, text="Get Details", command=get_location, font=("Helvetica", 14), bg="#4CAF50", fg="white", activebackground="#2E8B57", activeforeground="white")
get_location_button.pack(pady=10)


root.configure(bg="#F5F5F5")
root.geometry("600x500")


root.mainloop()
