from _flags import TARGET_SIZE
import colorsys, math

HUE_BAGAT = 0.1
SAT_BAGAT = 0.1
VAL_BAGAT = 0.1

# Returns a number between 0.0 and 1.0 for likeness
def compare(original, flag):
    score = 0
    pixelcount = 0
    for y in range(TARGET_SIZE[1]):
        for x in range(TARGET_SIZE[0]):
            original_pixel = original.getpixel((x, y))
            flag_pixel = flag.getpixel((x, y))
            score += _pixel_compare(original_pixel, flag_pixel)
            pixelcount += 1
    
    if not pixelcount:
        return 0

    return score / pixelcount


def _pixel_compare(original_pixel, flag_pixel):
    ohue, osat, oval = colorsys.rgb_to_hsv(original_pixel[0]/255, original_pixel[1]/255, original_pixel[2]/255)
    fhue, fsat, fval = colorsys.rgb_to_hsv(flag_pixel[0]/255, flag_pixel[1]/255, flag_pixel[2]/255)

    if ohue + HUE_BAGAT > fhue or ohue - HUE_BAGAT < fhue:
        hue_sim = 1 - (abs((ohue - fhue)) - HUE_BAGAT)
    else:
        hue_sim = 1
    
    if osat + SAT_BAGAT > fsat or osat - SAT_BAGAT < fsat:
        sat_sim = 1 - (abs((osat - fsat)) - SAT_BAGAT)
    else:
        sat_sim = 1
    
    if oval + VAL_BAGAT > fval or oval - VAL_BAGAT < fval:
        val_sim = 1 - (abs((oval - fval)) - VAL_BAGAT)
    else:
        val_sim = 1

    return (hue_sim * sat_sim * val_sim) ** (1/3)