# Global variable to count modifications
compteur_modifs = 0

# Constant target value (from instructions)
V_CIBLE = 7
def filtrer_valeurs(liste):
    global compteur_modifs  # Access the global variable
    
    # Iterate through the list using index
    for i in range(len(liste)):
        # Check if current element is greater than V_CIBLE
        if liste[i] > V_CIBLE:
            liste[i] = V_CIBLE
            # Increment modification counter
            compteur_modifs += 1
def processus_examen():
    global ListeExam
    filtrer_valeurs(ListeExam)
    
    # Display results
    print("=" * 50)
    print("📊 PROCESSUS EXAMEN - RESULTS")
    print("=" * 50)
    print(f"Modified List: {ListeExam}")
    print(f"Total modifications: {compteur_modifs}")
    print("=" * 50)

ListeExam = [15, 8, 22, 10, 4]

# Display initial state
print("=" * 50)
print("📋 INITIAL STATE")
print("=" * 50)
print(f"V_CIBLE = {V_CIBLE}")
print(f"Initial List: {ListeExam}")
print(f"Initial counter: {compteur_modifs}")

# Run the examination process
processus_examen()

