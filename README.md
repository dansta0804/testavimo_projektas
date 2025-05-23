# Skaliarinių sandaugų skaičiavimas

Repozitorijoje saugomi failai, kurie yra susiję su skaliarinių sandaugų skaičiavimo programa bei jos testavimu.
Skaliarines sandaugas skaičiuojanti programa yra parašyta Python programavimo kalba.

### Programos veikimas:
Pagrindinė programa ***vdot.py*** nuskaito direktorijoje ***Tests/Inputs*** esančius .dat failus, kuriuose yra aprašyti
vektoriai, apskaičiuoja šių vektorių sandaugas ir gautus rezultatus įrašo į direktoriją ***Tests/Outputs/Actual***.

### Direktorijų aprašymai:
- **Tests/** - ši direktorija yra skirta pagrindinės ***vdot.py*** programos testavimui, įvesties duomenų bei išvesties
rezultatų saugojimui. Direktoriją sudaro trys vaikinės direktorijos:
   - **Tests/** - repozitorijoje saugomi vienetiniai testai, skirti ***vdot.py*** programos testavimui;
   - **Inputs/** - repozitorijoje saugomi testavimui skirti įvesties duomenys (.dat faili);
   - **Outputs/** - repozitorijoje saugomi ***vdot.py*** programos išvesties rezultatai, kuriuos yra tikimąsi gauti,
   naudojant **Inputs/** direktorijoje naudojamus įvesties duomenis (**Outputs/Exptected** direktorija), bei rezultatai,
   kurie buvo gauti praleidus testus iš **Tests/** direktorijos (**Outputs/Actual** direktorija).