import sys
from pyswip import Prolog

def init_planets_database():
    """Initializes the Prolog engine and injects the Planets Database facts and rules."""
    prolog = Prolog()

    # --- 1. Database Facts ---
    
    # planet(Name, OrderFromSun, Type, HasRings)
    prolog.assertz("planet(mercury, 1, terrestrial, no)")
    prolog.assertz("planet(venus, 2, terrestrial, no)")
    prolog.assertz("planet(earth, 3, terrestrial, no)")
    prolog.assertz("planet(mars, 4, terrestrial, no)")
    prolog.assertz("planet(jupiter, 5, gas_giant, yes)")
    prolog.assertz("planet(saturn, 6, gas_giant, yes)")
    prolog.assertz("planet(uranus, 7, ice_giant, yes)")
    prolog.assertz("planet(neptune, 8, ice_giant, yes)")

    # --- 2. Custom Query Rules ---
    
    # Rule to find if a planet is closer to the Sun than another
    prolog.assertz("closer_to_sun(P1, P2) :- planet(P1, O1, _, _), planet(P2, O2, _, _), O1 < O2")
    
    # Rule to find all planets of a specific structural composition type
    prolog.assertz("planets_by_type(Type, Name) :- planet(Name, _, Type, _)")
    
    # Rule to identify planets that feature ring systems
    prolog.assertz("planets_with_rings(Name) :- planet(Name, _, _, yes)")

    return prolog

def parse_atom(atom):
    """Utility helper to process incoming raw byte atoms from Prolog safely."""
    if isinstance(atom, bytes):
        return atom.decode('utf-8')
    return str(atom)

def format_name(raw_string):
    """Capitalizes names for polished console display presentation."""
    return raw_string.replace('_', ' ').title()

def main():
    try:
        prolog = init_planets_database()
    except Exception as e:
        print(f"Engine connection failed: {e}. Make sure SWI-Prolog is installed and added to your system PATH.")
        sys.exit(1)

    print("=" * 65)
    print("                PROLOG PLANETS KNOWLEDGE BASE")
    print("=" * 65)

    # --- Query 1: Find all Terrestrial Planets ---
    target_type = "terrestrial"
    print(f"Query: Listing all planets with composition type [{target_type.upper()}]:")
    
    results_1 = list(prolog.query(f"planets_by_type({target_type}, Name)"))
    for match in results_1:
        planet_name = parse_atom(match['Name'])
        print(f"  -> {format_name(planet_name)}")
    print("-" * 65)

    # --- Query 2: Find all Planets that have Planetary Rings ---
    print("Query: Listing all planets that feature Ring Systems:")
    
    results_2 = list(prolog.query("planets_with_rings(Name)"))
    for match in results_2:
        planet_name = parse_atom(match['Name'])
        print(f"  -> {format_name(planet_name)}")
    print("-" * 65)

    # --- Query 3: Check relative order (Is Mars closer to the sun than Saturn?) ---
    p1, p2 = "mars", "saturn"
    print(f"Query: Is {format_name(p1)} closer to the Sun than {format_name(p2)}?")
    
    results_3 = list(prolog.query(f"closer_to_sun({p1}, {p2})"))
    if results_3:
        print("  -> Yes, that relationship is logically TRUE.")
    else:
        print("  -> No, that relationship is logically FALSE.")
        
    print("=" * 65)

if __name__ == "__main__":
    main()
