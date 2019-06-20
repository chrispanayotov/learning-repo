measurement = float(input())
input_unit = str(input())
output_unit = str(input())

m_to_mm = measurement * 1000
mm_to_m = measurement / 1000
m_to_cm = measurement * 100
cm_to_m = measurement / 100
cm_to_mm = measurement * 10
mm_to_cm = measurement / 10

if input_unit == 'mm' and output_unit == 'm':
    measurement = mm_to_m
elif input_unit == 'm' and output_unit == 'mm':
    measurement = m_to_mm
elif input_unit == 'm' and output_unit == 'cm':
    measurement = m_to_cm
elif input_unit == 'cm' and output_unit == 'm':
    measurement = cm_to_m
elif input_unit == 'cm' and output_unit == 'mm':
    measurement = cm_to_mm
elif input_unit == 'mm' and output_unit == 'cm':
    measurement = mm_to_cm

print(f"{measurement:.3f}")

