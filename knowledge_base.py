knowledge_base = diseases = [
    """
    Disease: Influenza (Flu)
    
    Description: A contagious respiratory illness caused by influenza viruses. It primarily affects the nose, throat, and sometimes the lungs. The flu can range from mild to severe and can even lead to hospitalization and death, especially in vulnerable populations.
    
    Causes: Influenza viruses, which can be of different strains (e.g., A, B, C). These viruses are constantly changing, making annual vaccination necessary to target the prevalent strains.
    
    Symptoms: Fever, cough, sore throat, body aches, fatigue, headache, chills, and sometimes gastrointestinal symptoms like vomiting and diarrhea.
    
    Prevention: Annual flu vaccination is the most effective preventive measure. Good hygiene practices, such as frequent handwashing and avoiding close contact with sick individuals, also help prevent transmission.
    
    Cure: Supportive care to manage symptoms includes rest, hydration, and over-the-counter pain relievers. Antiviral medications like oseltamivir (Tamiflu) can help reduce the severity and duration of symptoms if taken early in the illness.
    
    Drug Prediction: Oseltamivir (Tamiflu) is a commonly used antiviral drug for treating influenza infections. It works by inhibiting the virus's ability to spread within the body.
    """,
    """
    Disease: Tuberculosis (TB)
    
    Description: A bacterial infection caused by Mycobacterium tuberculosis that primarily affects the lungs but can also target other parts of the body.
    
    Causes: Mycobacterium tuberculosis bacteria spread through the air when an infected person coughs or sneezes, or through close contact.
    
    Symptoms: Persistent cough, chest pain, fatigue, weight loss, fever, night sweats, and sometimes coughing up blood.
    
    Prevention: Proper ventilation, avoiding close contact with infected individuals, and completing a full course of treatment if infected.
    
    Cure: Treated with antibiotics over an extended period. Drug-resistant TB requires specialized medications.
    
    Drug Prediction: Common drugs include isoniazid, rifampin, pyrazinamide, and ethambutol.
    """,
    """
    Disease: Malaria
    
    Description: A mosquito-borne disease caused by Plasmodium parasites. It leads to flu-like symptoms and can be life-threatening if not treated.
    
    Causes: Female Anopheles mosquitoes transmit Plasmodium parasites through their bites.
    
    Symptoms: Fever, chills, sweats, headache, muscle aches, and fatigue. Severe cases can lead to organ failure and death.
    
    Prevention: Using insect repellents, bed nets, and antimalarial medications in endemic areas.
    
    Cure: Antimalarial medications like chloroquine, artemisinin-based combination therapies (ACTs), and others are used for treatment.
    
    Drug Prediction: Artemisinin-based combination therapies (ACTs) are the recommended treatment.
    """,
    """
    Disease: Diabetes
    
    Description: A chronic metabolic disorder characterized by high blood sugar levels due to insufficient insulin production or insulin resistance.
    
    Causes: Type 1 diabetes is autoimmune, while type 2 is linked to obesity and inactivity.
    
    Symptoms: Increased thirst, frequent urination, fatigue, blurred vision, slow wound healing, and unexplained weight loss.
    
    Prevention: Type 1 diabetes cannot be prevented. Type 2 diabetes can be prevented through a healthy lifestyle.
    
    Cure: Type 1 diabetes is managed with insulin. Type 2 diabetes can be managed with lifestyle changes and medications.
    
    Drug Prediction: Common classes include metformin, sulfonylureas, DPP-4 inhibitors, and insulin.
    """,
    """
    Disease: Cancer
    
    Description: Refers to a group of diseases characterized by uncontrolled cell growth and potential to invade other tissues.
    
    Causes: Genetics, exposure to carcinogens, and lifestyle factors contribute to different types of cancer.
    
    Symptoms: Vary based on type and stage, including unexplained weight loss, fatigue, pain, and changes in skin or bowel habits.
    
    Prevention: Avoiding tobacco, healthy diet, exercise, and limiting sun exposure.
    
    Cure: Treatment options include surgery, chemotherapy, radiation therapy, targeted therapy, and immunotherapy.
    
    Drug Prediction: Regimens vary based on specific cancer type and characteristics.
    """,
    """
    Disease: Alzheimer's Disease
    
    Description: A progressive neurodegenerative disorder leading to memory loss, cognitive decline, and behavioral changes.
    
    Causes: Genetics, age, abnormal protein deposits (amyloid plaques, tau tangles) contribute.
    
    Symptoms: Memory loss, confusion, mood changes, difficulty with tasks, and language problems.
    
    Prevention: Mental and physical activity, healthy diet, social connections may reduce risk.
    
    Cure: No cure, treatments manage symptoms and slow progression.
    
    Drug Prediction: Cholinesterase inhibitors (donepezil, rivastigmine) and NMDA receptor antagonist (memantine) are common medications.
    """,
    """
    Disease: Parkinson's Disease
    
    Description: A progressive neurological disorder affecting movement. Tremors, stiffness, and coordination difficulties are common.
    
    Causes: Loss of dopamine-producing cells in the brain. Genetics and environment play roles.
    
    Symptoms: Tremors, bradykinesia (slow movement), muscle stiffness, postural instability, speech changes.
    
    Prevention: No known prevention methods.
    
    Cure: No cure, medications like levodopa and dopamine agonists manage symptoms.
    
    Drug Prediction: Levodopa helps increase dopamine levels in the brain.
    """,
    """
    Disease: HIV/AIDS
    
    Description: Weakens the immune system, potentially leading to AIDS. Transmitted through certain body fluids.
    
    Causes: Contact with infected body fluids, such as blood, semen, vaginal fluids, breast milk.
    
    Symptoms: Early stages may have flu-like symptoms. Later stages can cause opportunistic infections, weight loss, and severe illnesses.
    
    Prevention: Safe sex practices, needle exchange, pre-exposure prophylaxis (PrEP) reduce transmission risk.
    
    Cure: No cure, antiretroviral therapy (ART) manages the virus and slows progression.
    
    Drug Prediction: ART involves drug combinations, including nucleoside reverse transcriptase inhibitors (NRTIs), non-nucleoside reverse transcriptase inhibitors (NNRTIs), protease inhibitors, integrase inhibitors.
    """,
    """
    Disease: Cholera
    
    Description: An infectious disease causing severe diarrhea and dehydration. It spreads through contaminated water and food.
    
    Causes: Infection with the bacterium Vibrio cholerae from contaminated water and food.
    
    Symptoms: Profuse watery diarrhea, vomiting, dehydration, electrolyte imbalances.
    
    Prevention: Clean water, proper sanitation, good hygiene, and vaccination in endemic areas.
    
    Cure: Rehydration with oral rehydration solution (ORS) and in severe cases, intravenous fluids. Antibiotics may also be used.
    
    Drug Prediction: Antibiotics like doxycycline or azithromycin are used to shorten the duration and severity of symptoms.
    """,
    """
    Disease: Ebola Virus Disease
    
    Description: A severe, often fatal illness caused by the Ebola virus. It leads to fever, bleeding, organ failure, and high mortality rates.
    
    Causes: Infection with the Ebola virus through direct contact with the blood, secretions, organs, or other bodily fluids of infected people or animals.
    
    Symptoms: Sudden fever, fatigue, muscle pain, headache, followed by vomiting, diarrhea, rash, impaired kidney and liver function, and in some cases, internal and external bleeding.
    
    Prevention: Avoiding contact with infected people or animals, practicing good hygiene, and using protective gear in healthcare settings.
    
    Cure: Supportive care, including fluid and electrolyte replacement. No specific antiviral treatment is approved, but experimental treatments may be used in certain cases.
    
    Drug Prediction: Various experimental treatments have been explored, including monoclonal antibodies and antiviral drugs like remdesivir.
    """,
        """
    Disease: Measles
    
    Description: A highly contagious viral infection causing fever, rash, and other symptoms.
    
    Causes: Measles virus transmitted through respiratory droplets.
    
    Symptoms: Fever, cough, runny nose, red eyes, rash.
    
    Prevention: Measles vaccination is essential to prevent outbreaks.
    
    Cure: Supportive care to manage symptoms.
    
    """,
        """
    Disease: Hepatitis
    
    Description: Inflammation of the liver, often caused by viral infections.
    
    Causes: Hepatitis viruses (A, B, C, D, E), alcohol, toxins.
    
    Symptoms: Jaundice, fatigue, abdominal pain, dark urine.
    
    Prevention: Vaccination (Hepatitis A, B), safe sex, avoiding sharing needles.
    
    Cure: Antiviral medications, lifestyle changes.
    
    """,
        """
    Disease: Pneumonia
    
    Description: Infection causing inflammation of the air sacs in the lungs.
    
    Causes: Bacteria, viruses, fungi.
    
    Symptoms: Cough, fever, difficulty breathing, chest pain.
    
    Prevention: Vaccination (pneumococcal, flu), good hygiene.
    
    Cure: Antibiotics (bacterial pneumonia), antivirals (viral pneumonia).
    
    """,
        """
    Disease: Asthma
    
    Description: Chronic lung condition causing airway inflammation and constriction.
    
    Causes: Genetics, allergies, environmental factors.
    
    Symptoms: Wheezing, shortness of breath, coughing.
    
    Prevention: Avoiding triggers, proper medication use.
    
    Cure: Inhalers (bronchodilators, corticosteroids), long-term management.
    
    """,
        """
    Disease: Arthritis
    
    Description: Inflammation of joints, causing pain and stiffness.
    
    Causes: Genetics, age, autoimmune factors.
    
    Symptoms: Joint pain, swelling, reduced range of motion.
    
    Prevention: Regular exercise, maintaining a healthy weight.
    
    Cure: Medications, physical therapy, joint protection.
    
    """,
        """
    Disease: Stroke
    
    Description: Disruption of blood flow to the brain, leading to brain damage.
    
    Causes: Ischemic (blood clot), hemorrhagic (bleeding) strokes.
    
    Symptoms: Sudden numbness, confusion, trouble speaking, dizziness.
    
    Prevention: Blood pressure control, healthy lifestyle.
    
    Cure: Immediate medical treatment to restore blood flow.
    
    """,
        """
    Disease: Schizophrenia
    
    Description: Chronic mental disorder with disturbances in perception, thought, and behavior.
    
    Causes: Genetic, environmental factors, brain chemistry.
    
    Symptoms: Hallucinations, delusions, disorganized thinking.
    
    Prevention: Early intervention, managing stress.
    
    Cure: Medications (antipsychotics), therapy.
    
    """,
        """
    Disease: Epilepsy
    
    Description: Neurological disorder causing recurrent seizures.
    
    Causes: Genetic factors, brain injury, infections.
    
    Symptoms: Seizures, loss of consciousness, convulsions.
    
    Prevention: Medications, avoiding triggers.
    
    Cure: Management with antiepileptic drugs.
    
    """,
        """
    Disease: Multiple Sclerosis
    
    Description: Autoimmune disease affecting the central nervous system.
    
    Causes: Genetics, immune system dysfunction.
    
    Symptoms: Fatigue, numbness, difficulty walking.
    
    Prevention: Unknown, but healthy lifestyle may help.
    
    Cure: No cure, disease-modifying therapies.
    
    """,
        """
    Disease: Osteoporosis
    
    Description: Bone disease causing weakened and brittle bones.
    
    Causes: Aging, hormonal changes, low calcium intake.
    
    Symptoms: Bone fractures, loss of height.
    
    Prevention: Adequate calcium, vitamin D, weight-bearing exercise.
    
    Cure: Medications, lifestyle changes.
    """,

        """
    Disease: Leukemia
    
    Description: A type of cancer affecting blood cells, particularly white blood cells.
    
    Causes: Genetic mutations, radiation, exposure to certain chemicals.
    
    Symptoms: Fatigue, anemia, bleeding, susceptibility to infections.
    
    Prevention: Unknown, healthy lifestyle may help reduce risk.
    
    Cure: Chemotherapy, stem cell transplant.
    
    """,
        """
    Disease: Crohn's Disease
    
    Description: Inflammatory bowel disease causing inflammation of the digestive tract.
    
    Causes: Genetic, immune system dysfunction.
    
    Symptoms: Abdominal pain, diarrhea, weight loss.
    
    Prevention: No known prevention methods.
    
    Cure: Medications (anti-inflammatory, immunosuppressants).
    
    """,
        """
    Disease: Hypertension
    
    Description: Chronic condition characterized by high blood pressure.
    
    Causes: Genetic factors, lifestyle (diet, exercise), stress.
    
    Symptoms: Often asymptomatic, headaches, fatigue.
    
    Prevention: Healthy lifestyle, medication if necessary.
    
    Cure: Management through lifestyle changes, medications.
    
    """,
        """
    Disease: Cystic Fibrosis
    
    Description: Genetic disorder affecting the lungs and digestive system.
    
    Causes: Inherited genetic mutations.
    
    Symptoms: Persistent cough, lung infections, digestive issues.
    
    Prevention: Genetic counseling.
    
    Cure: No cure, management with medications, therapies.
    
    """,
        """
    Disease: Dengue Fever
    
    Description: Mosquito-borne viral infection causing flu-like symptoms.
    
    Causes: Aedes mosquitoes transmit the dengue virus.
    
    Symptoms: High fever, severe headache, joint and muscle pain.
    
    Prevention: Mosquito control, avoiding mosquito bites.
    
    Cure: Supportive care, hydration.
    
    """,
        """
    Disease: Leprosy
    
    Description: Chronic bacterial infection affecting the skin and nerves.
    
    Causes: Infection with Mycobacterium leprae.
    
    Symptoms: Skin lesions, numbness, muscle weakness.
    
    Prevention: Early diagnosis and treatment.
    
    Cure: Multi-drug therapy.
    
    """,
        """
    Disease: Rabies
    
    Description: Viral infection affecting the central nervous system.
    
    Causes: Bite of a rabid animal.
    
    Symptoms: Fever, agitation, hallucinations, paralysis.
    
    Prevention: Vaccination (pre-exposure, post-exposure).
    
    Cure: No cure once symptoms appear, preventive treatment after exposure.
    
    """,
        """
    Disease: Glaucoma
    
    Description: Eye condition damaging the optic nerve, often due to high eye pressure.
    
    Causes: Increased eye pressure, genetics.
    
    Symptoms: Gradual loss of peripheral vision.
    
    Prevention: Regular eye exams, managing eye pressure.
    
    Cure: Medications, laser therapy, surgery.
    
    """,
        """
    Disease: Hemophilia
    
    Description: Genetic disorder impairing blood clotting.
    
    Causes: Genetic mutations affecting clotting factors.
    
    Symptoms: Excessive bleeding, bruising.
    
    Prevention: Genetic counseling.
    
    Cure: Management with clotting factor replacement.
    
    """,
        """
    Disease: Melanoma
    
    Description: Aggressive form of skin cancer originating in melanocytes.
    
    Causes: UV radiation, genetic factors.
    
    Symptoms: Asymmetrical moles, changes in existing moles.
    
    Prevention: Sun protection, avoiding tanning beds.
    
    Cure: Surgical removal, immunotherapy, targeted therapy.
    
    """,

    """
    Disease: Polio
    
    Description: Polio, also known as poliomyelitis, is a highly infectious viral disease that can cause paralysis and even death. It primarily affects the nervous system, leading to muscle weakness or paralysis.
    
    Causes: Polio is caused by the poliovirus, which is highly contagious and spreads through contaminated food, water, and direct contact with an infected person's saliva or feces.
    
    Symptoms: Most cases are asymptomatic or cause mild flu-like symptoms. In severe cases, it can lead to muscle weakness, paralysis, and difficulty breathing.
    
    Prevention: Polio vaccines have been highly effective in preventing the disease. Vaccination campaigns have led to a significant reduction in polio cases globally.
    
    Cure: There is no cure for polio, but supportive care can help manage symptoms. Rehabilitation and physical therapy are often used to improve muscle function in affected individuals.
    
    """,
    """
    Disease: Psoriasis
    
    Description: Psoriasis is a chronic autoimmune skin disorder characterized by red, scaly patches on the skin's surface. It often affects elbows, knees, and scalp but can appear anywhere on the body.
    
    Causes: The exact cause is not fully understood, but it involves immune system dysfunction and genetic factors.
    
    Symptoms: Raised, inflamed patches covered with silvery-white scales, itching, and discomfort.
    
    Prevention: There is no known way to prevent psoriasis, but managing triggers and stress can help reduce flare-ups.
    
    Cure: There is no cure for psoriasis, but treatments aim to control symptoms. Topical treatments, phototherapy, and systemic medications are used based on severity.
    
    """,

    
    """
    Disease: Sickle Cell Disease
    
    Description: Sickle cell disease is a genetic disorder that affects hemoglobin, causing red blood cells to become misshapen and break down more easily, leading to anemias and other complications.
    
    Causes: Inherited genetic mutations affecting the hemoglobin molecule.
    
    Symptoms: pain episodes (crisis), fatigue, susceptibility to infections.
    
    Prevention: Genetic counseling and testing for carriers can help individuals make informed family planning decisions.
    
    Cure: While there is no cure, treatments include managing symptoms and complications. Blood transfusions, medications, and stem cell transplants can be used.
    
    """,
    """
    Disease: Ulcerative Colitis
    
    Description: Ulcerative colitis is a chronic inflammatory bowel disease that primarily affects the colon and rectum. It leads to ulcers, inflammation, and discomfort.
    
    Causes: The exact cause is unclear, but it involves a combination of genetic, immune, and environmental factors.
    
    Symptoms: Diarrhea, abdominal pain, rectal bleeding, weight loss.
    
    Prevention: There is no known prevention for ulcerative colitis.
    
    Cure: While there is no cure, medications such as anti-inflammatory drugs, immunosuppressants, and biologics can help manage symptoms. In severe cases, surgery may be necessary.
    
    """,
    """
    Disease: Huntington's Disease
    
    Description: Huntington's disease is a progressive genetic disorder that causes the breakdown of nerve cells in the brain, leading to motor, cognitive, and psychiatric symptoms.
    
    Causes: Inherited genetic mutation in the HTT gene.
    
    Symptoms: Involuntary movements, cognitive decline, mood changes, difficulty with coordination.
    
    Prevention: Genetic testing and counseling for those with a family history can help individuals make informed decisions.
    
    Cure: There is no cure for Huntington's disease, but treatments focus on managing symptoms and improving quality of life.
    
    """,
    """
    Disease: Celiac Disease
    
    Description: Celiac disease is an autoimmune disorder in which the consumption of gluten triggers an immune response, damaging the small intestine and affecting nutrient absorption.
    
    Causes: Genetic predisposition, consumption of gluten (found in wheat, barley, rye).
    
    Symptoms: Digestive symptoms, fatigue, skin rash (dermatitis herpetiformis), nutrient deficiencies.
    
    Prevention: The only prevention is adhering to a strict gluten-free diet.
    
    Cure: There is no cure, but following a gluten-free diet is essential to managing symptoms and preventing complications.
    
    """,

        """
    Disease: Gout
    
    Description: Gout is a type of inflammatory arthritis caused by the accumulation of uric acid crystals in the joints. It leads to sudden and severe episodes of pain and inflammation, often affecting the joint of the big toe.
    
    Causes: Gout develops when there's an excess of uric acid in the blood, leading to the formation of urate crystals in the joints. This can result from overproduction of uric acid or reduced excretion by the kidneys.
    
    Symptoms: Acute pain, swelling, redness, and warmth in the affected joint. Gout attacks often occur suddenly, mostly during the night, and can last for several days.
    
    Prevention: Maintaining a healthy lifestyle, including a balanced diet, limited alcohol intake, and staying hydrated, can help prevent gout attacks. Avoiding foods rich in purines, such as red meat and seafood, can also be beneficial.
    
    Cure: While there's no cure for gout, it can be managed effectively. During acute attacks, medications like nonsteroidal anti-inflammatory drugs (NSAIDs), colchicine, or corticosteroids can alleviate pain and inflammation. Long-term management involves lifestyle changes, dietary modifications, and medications to lower uric acid levels.
    
    """,
        """
    Disease: Ovarian Cancer
    
    Description: Ovarian cancer is a type of cancer that starts in the ovaries, often diagnosed at an advanced stage due to its subtle or absent early symptoms. It can spread to other parts of the abdomen and pelvis.
    
    Causes: The exact cause is unclear, but certain risk factors include family history of ovarian, breast, or colon cancer, age, hormonal factors, and inherited gene mutations (BRCA1, BRCA2).
    
    Symptoms: Early symptoms are often vague, including abdominal bloating, pelvic discomfort, changes in bowel habits, and frequent urination. As the disease progresses, symptoms may become more noticeable.
    
    Prevention: Regular pelvic examinations, genetic counseling for individuals with family history, and being aware of risk factors are essential for early detection and prevention.
    
    Cure: Treatment depends on the stage and extent of spread. Surgery to remove the tumor and affected tissues, followed by chemotherapy, is the standard approach. Targeted therapies and immunotherapy are also being explored.
    
    """,
        """
    Disease: Pancreatitis
    
    Description: Pancreatitis is the inflammation of the pancreas, a gland responsible for producing digestive enzymes and hormones like insulin. It can range from mild to severe and may be acute or chronic.
    
    Causes: Gallstones, excessive alcohol consumption, high triglyceride levels, certain medications, and infections can trigger pancreatitis. Chronic pancreatitis can result from repeated bouts of acute pancreatitis.
    
    Symptoms: Abdominal pain that may radiate to the back, nausea, vomiting, fever, and a tender abdomen. Severe cases can lead to complications like organ failure and infection.
    
    Prevention: Limiting alcohol consumption, maintaining a healthy weight, managing gallstones, and avoiding triggers can help prevent pancreatitis.
    
    Cure: Treatment depends on the underlying cause and severity. Acute pancreatitis often requires hospitalization, fasting, and supportive care. Chronic pancreatitis management involves pain control, enzyme replacement, and dietary modifications.
    
    """,
        """
    Disease: Gastritis
    
    Description: Gastritis is the inflammation of the stomach lining, which can lead to discomfort, pain, and digestive symptoms. It can be acute (short-term) or chronic (long-term).
    
    Causes: Gastritis can result from infection with Helicobacter pylori bacteria, excessive use of nonsteroidal anti-inflammatory drugs (NSAIDs), excessive alcohol consumption, stress, or autoimmune reactions.
    
    Symptoms: Abdominal pain or discomfort, nausea, vomiting, loss of appetite, bloating, and indigestion.
    
    Prevention: Avoiding irritants like alcohol and NSAIDs, managing stress, and maintaining a healthy diet can help prevent gastritis.
    
    Cure: Treatment involves addressing the underlying cause. For H. pylori-related gastritis, antibiotics and acid-suppressing medications are used. Avoiding trigger substances, reducing stress, and making dietary changes can also help manage symptoms.
    
    """,

        """
    Disease: Lupus
    
    Description: Lupus, or systemic lupus erythematosus (SLE), is a chronic autoimmune disease that can affect various parts of the body, including the skin, joints, and internal organs.
    
    Causes: The exact cause is unknown, but genetics, hormonal factors, and environmental triggers are thought to contribute.
    
    Symptoms: Fatigue, joint pain, skin rashes, fever, and in severe cases, organ involvement.
    
    Prevention: While lupus can't be prevented, managing stress, avoiding excessive sun exposure, and maintaining a healthy lifestyle can help reduce symptoms.
    
    Cure: There's no cure, but treatment focuses on managing symptoms. Medications, lifestyle changes, and regular medical monitoring are common approaches.
    
    """,
        """
    Disease: Endometriosis
    
    Description: Endometriosis is a chronic condition where tissue similar to the lining of the uterus grows outside the uterus, leading to pain and sometimes fertility issues.
    
    Causes: The exact cause is unclear, but genetics and hormonal factors are believed to play a role.
    
    Symptoms: Pelvic pain, painful periods, pain during intercourse, and in severe cases, infertility.
    
    Prevention: Early diagnosis and treatment can help manage symptoms and prevent complications.
    
    Cure: While there's no cure, treatment options include pain management, hormonal therapy, and in some cases, surgery to remove endometrial tissue.
    
    """,
        """
    Disease: Anemia
    
    Description: Anemia is a condition characterized by a reduced number of red blood cells or low hemoglobin levels, leading to reduced oxygen transport in the body.
    
    Causes: Anemia can result from various factors, including iron deficiency, vitamin B12 deficiency, chronic diseases, and blood loss.
    
    Symptoms: Fatigue, weakness, pale skin, shortness of breath, and cold hands and feet.
    
    Prevention: Maintaining a balanced diet rich in iron, vitamins, and minerals can help prevent anemia.
    
    Cure: Treatment depends on the underlying cause and severity. It may involve dietary changes, iron supplements, and addressing any underlying health conditions.
    
    """,
        """
    Disease: Osteoarthritis
    
    Description: Osteoarthritis is a degenerative joint disease characterized by the breakdown of joint cartilage and bone, leading to pain and reduced mobility.
    
    Causes: Age, joint injury, obesity, and genetic factors contribute to the development of osteoarthritis.
    
    Symptoms: Joint pain, stiffness, swelling, and decreased range of motion.
    
    Prevention: Maintaining a healthy weight, exercising regularly, and avoiding joint injuries can help prevent osteoarthritis.
    
    Cure: There's no cure, but treatments include pain management, physical therapy, and in some cases, joint replacement surgery.
    
    """,
        """
    Disease: Heart Disease
    
    Description: Heart disease refers to various conditions that affect the heart's function, including coronary artery disease, heart failure, and arrhythmias.
    
    Causes: Risk factors include high blood pressure, high cholesterol, smoking, diabetes, and family history.
    
    Symptoms: Chest pain, shortness of breath, fatigue, irregular heartbeat, and swelling in the legs.
    
    Prevention: A healthy lifestyle, including a balanced diet, regular exercise, and avoiding tobacco, can reduce the risk of heart disease.
    
    Cure: Treatment depends on the specific condition and severity. It may involve medications, lifestyle changes, and medical procedures.
    
    """,
        """
    Disease: Kidney Stones
    
    Description: Kidney stones are hard deposits that form in the kidneys and can cause severe pain when they move through the urinary tract.
    
    Causes: Dehydration, certain medical conditions, and dietary factors can contribute to kidney stone formation.
    
    Symptoms: Intense pain in the back or side, pain during urination, and blood in the urine.
    
    Prevention: Staying hydrated, maintaining a balanced diet, and managing underlying conditions can help prevent kidney stones.
    
    Cure: Small stones may pass on their own with pain management. Larger stones may require medical intervention, such as lithotripsy or surgery.
    
    """,
        """
    Disease: Fibromyalgia
    
    Description: Fibromyalgia is a chronic disorder characterized by widespread musculoskeletal pain, fatigue, and sleep disturbances.
    
    Causes: The exact cause is unknown, but genetics, infections, and physical or emotional trauma may contribute.
    
    Symptoms: Widespread pain, fatigue, sleep disturbances, and cognitive difficulties (often called "fibro fog").
    
    Prevention: While fibromyalgia can't be prevented, managing stress, getting regular exercise, and practicing good sleep hygiene can help manage symptoms.
    
    Cure: There's no cure, but treatment involves symptom management through medications, physical therapy, and lifestyle adjustments.
    
    """,
        """
    Disease: Leishmaniasis
    
    Description: Leishmaniasis is a vector-borne disease caused by parasites of the Leishmania genus, leading to skin sores or systemic infections.
    
    Causes: Sandfly bites transmit Leishmania parasites.
    
    Symptoms: Skin sores, fever, weight loss in the systemic form.
    
    Prevention: Avoiding sandfly bites through protective clothing, bed nets, and insect repellents.
    
    Cure: Treatment depends on the form of leishmaniasis. Skin sores can be treated with local treatments, while systemic infections require medications.
    
    """,
        """
    Disease: Pneumothorax
    
    Description: Pneumothorax is a condition where air accumulates in the space between the lungs and chest wall, causing lung collapse.
    
    Causes: Spontaneous pneumothorax can occur without a clear cause, while traumatic pneumothorax results from chest injuries.
    
    Symptoms: Sudden chest pain, difficulty breathing, and rapid heart rate.
    
    Prevention: Preventive measures depend on the underlying cause. Traumatic pneumothorax can be minimized by avoiding chest injuries.
    
    Cure: Small, uncomplicated pneumothoraxes may resolve on their own. Larger or recurrent cases may require chest tube insertion to remove air.
    
    """,
        """
    Disease: Chlamydia
    
    Description: Chlamydia is a common sexually transmitted infection caused by the bacterium Chlamydia trachomatis.
    
    Causes: Sexual contact with an infected person.
    
    Symptoms: Often asymptomatic, but can cause genital discharge, pain during urination, and pelvic inflammatory disease (PID) in women.
    
    Prevention: Safe sex practices, including condom use and regular STI screenings.
    
    Cure: Chlamydia can be treated and cured with antibiotics. Prompt treatment is essential to prevent complications.
    
    """,

        """
    Disease: Syphilis
    
    Description: Syphilis is a sexually transmitted infection caused by the bacterium Treponema pallidum. It progresses through stages and can cause serious complications if left untreated.
    
    Causes: Sexual contact with an infected person, including oral, genital, or anal contact.
    
    Symptoms: Primary stage - painless sores (chancre), secondary stage - skin rash, mucous membrane lesions, latent stage - no symptoms, tertiary stage - severe complications affecting organs like the heart and brain.
    
    Prevention: Safe sex practices, including condom use and regular STI screenings.
    
    Cure: Syphilis can be treated and cured with antibiotics, especially in the early stages. Late-stage complications may require more extended treatment.
    
    """,
        """
    Disease: Gonorrhea
    
    Description: Gonorrhea is a common sexually transmitted infection caused by the bacterium Neisseria gonorrhoeae. It can affect various body parts, including the genitals, rectum, and throat.
    
    Causes: Sexual contact with an infected person, including oral, genital, or anal contact.
    
    Symptoms: Genital discharge, pain during urination, and in some cases, rectal or throat symptoms.
    
    Prevention: Safe sex practices, including condom use and regular STI screenings.
    
    Cure: Gonorrhea can be treated with antibiotics, but antibiotic-resistant strains are a concern. Prompt treatment is crucial to prevent complications.
    
    """,
        """
    Disease: Chikungunya
    
    Description: Chikungunya is a viral infection transmitted by mosquitoes. It causes fever, joint pain, and other flu-like symptoms.
    
    Causes: Aedes mosquitoes transmit the chikungunya virus.
    
    Symptoms: Sudden high fever, joint pain, muscle pain, headache, rash.
    
    Prevention: Mosquito control, using insect repellents, wearing protective clothing.
    
    Cure: Treatment focuses on relieving symptoms through rest, fluids, and pain relievers. Most people recover fully, but joint pain may persist.
    
    """,
        """
    Disease: Dengue Hemorrhagic Fever
    
    Description: Dengue hemorrhagic fever is a severe form of dengue fever, a mosquito-borne viral infection. It can lead to bleeding, shock, and organ failure.
    
    Causes: Aedes mosquitoes transmit the dengue virus.
    
    Symptoms: High fever, severe headache, joint and muscle pain, bleeding, abdominal pain.
    
    Prevention: Mosquito control, avoiding mosquito bites.
    
    Cure: Treatment involves supportive care, including fluid replacement. Severe cases require hospitalization and monitoring.
    
    """,
        """
    Disease: Alzheimer's Disease
    
    Description: Alzheimer's disease is a progressive neurological disorder that affects memory, thinking, and behavior. It's the most common cause of dementia.
    
    Causes: Complex interplay of genetic, environmental, and lifestyle factors.
    
    Symptoms: Memory loss, confusion, trouble with language, changes in mood and behavior.
    
    Prevention: While there's no surefire prevention, staying mentally and socially active, exercising regularly, and maintaining a healthy diet may help reduce the risk.
    
    Cure: There's no cure, but treatments and interventions can help manage symptoms and improve quality of life.
    
    """,
        """
    Disease: Amyotrophic Lateral Sclerosis (ALS)
    
    Description: ALS, also known as Lou Gehrig's disease, is a progressive neurodegenerative disorder that affects nerve cells in the brain and spinal cord, leading to muscle weakness and paralysis.
    
    Causes: The majority of cases are sporadic, but some are linked to genetic mutations.
    
    Symptoms: Muscle weakness, difficulty speaking, swallowing, and breathing.
    
    Prevention: There's no known prevention for ALS.
    
    Cure: There's no cure, and treatment focuses on managing symptoms and providing supportive care.
    
    """,
        """
    Disease: Bacterial Meningitis
    
    Description: Bacterial meningitis is the inflammation of the membranes surrounding the brain and spinal cord, typically caused by bacterial infections.
    
    Causes: Various bacteria, including Neisseria meningitidis and Streptococcus pneumoniae.
    
    Symptoms: Severe headache, fever, stiff neck, sensitivity to light, confusion.
    
    Prevention: Vaccination (bacterial strains like meningococcal vaccines), practicing good hygiene.
    
    Cure: Bacterial meningitis is a medical emergency. Early diagnosis and treatment with antibiotics are essential to prevent complications and death.
    
    """,
        """
    Disease: Barrett's Esophagus
    
    Description: Barrett's esophagus is a condition where the lining of the esophagus changes, increasing the risk of esophageal cancer.
    
    Causes: Chronic gastroesophageal reflux disease (GERD) is a major risk factor.
    
    Symptoms: Often asymptomatic, but GERD symptoms like heartburn and regurgitation may be present.
    
    Prevention: Managing GERD symptoms and risk factors can help prevent Barrett's esophagus.
    
    Cure: Regular monitoring and treatment of GERD can help manage the condition. In some cases, procedures to remove abnormal tissue may be necessary.
    
    """,
        """
    Disease: Bell's Palsy
    
    Description: Bell's palsy is a sudden, temporary paralysis or weakness of the muscles on one side of the face. It's often linked to viral infections.
    
    Causes: Herpes simplex virus or other viral infections affecting the facial nerve.
    
    Symptoms: Sudden facial droopiness, difficulty closing one eye, drooling, and changes in taste.
    
    Prevention: There's no known way to prevent Bell's palsy.
    
    Cure: Most cases resolve on their own within weeks to months. Steroids may be prescribed to speed up recovery.
    
    """,
        """
    Disease: Benign Prostatic Hyperplasia (BPH)
    
    Description: BPH is a non-cancerous enlargement of the prostate gland, leading to urinary symptoms in older men.
    
    Causes: Age-related hormonal changes, particularly an increase in dihydrotestosterone (DHT).
    
    Symptoms: Frequent urination, weak urine flow, difficulty starting and stopping urination.
    
    Prevention: Regular medical checkups and managing risk factors like obesity and sedentary lifestyle.
    
    Cure: Treatment options include medications, minimally invasive procedures, and surgery for severe cases.
    
    """,

        """
    Disease: Black Lung Disease (Coal Worker's Pneumoconiosis)
    
    Description: Black lung disease is a respiratory condition caused by long-term inhalation of coal dust, primarily affecting coal miners.
    
    Causes: Prolonged exposure to coal dust particles in coal mines.
    
    Symptoms: Chronic cough, shortness of breath, chest pain, and in advanced cases, progressive lung function decline.
    
    Prevention: Proper ventilation and use of protective equipment in coal mines.
    
    Cure: There's no cure, but early detection and quitting mining can slow the progression. Treatment focuses on managing symptoms and preventing complications.
    
    """,
        """
    Disease: Brucellosis
    
    Description: Brucellosis is a bacterial infection transmitted from animals to humans through contact with contaminated animal products or ingestion of unpasteurized dairy products.
    
    Causes: Bacteria of the Brucella genus.
    
    Symptoms: Fever, fatigue, muscle pain, joint pain, and in severe cases, complications affecting organs like the heart and liver.
    
    Prevention: Avoiding contact with infected animals and consuming only pasteurized dairy products.
    
    Cure: Treatment involves a combination of antibiotics, usually taken for several weeks. Relapses are possible.
    
    """,
        """
    Disease: Bulimia Nervosa
    
    Description: Bulimia nervosa is an eating disorder characterized by episodes of binge eating followed by compensatory behaviors like vomiting or excessive exercise.
    
    Causes: Complex interplay of genetic, psychological, and environmental factors.
    
    Symptoms: Binge eating, followed by guilt, shame, and compensatory behaviors to avoid weight gain.
    
    Prevention: Early intervention and psychotherapy can help prevent the development of bulimia.
    
    Cure: Treatment involves psychotherapy (such as cognitive-behavioral therapy), nutritional counseling, and sometimes medication. Recovery is possible with appropriate support.
    
    """,
        """
    Disease: Bunions
    
    Description: A bunion is a bony bump that forms at the base of the big toe, causing the big toe to point inward and crowding other toes.
    
    Causes: Genetic predisposition, tight-fitting shoes, and certain foot types.
    
    Symptoms: Bump on the side of the foot, pain, redness, and difficulty finding comfortable shoes.
    
    Prevention: Wearing well-fitting shoes and avoiding high heels can help prevent bunions.
    
    Cure: Treatment ranges from conservative measures like changing footwear and using orthotics to surgical correction in severe cases.
    
    """,
        """
    Disease: Carpal Tunnel Syndrome
    
    Description: Carpal tunnel syndrome is a condition where the median nerve becomes compressed as it passes through the wrist, leading to pain, numbness, and weakness in the hand.
    
    Causes: Repetitive hand movements, wrist injuries, and certain medical conditions.
    
    Symptoms: Numbness, tingling, pain, and weakness in the hand, especially at night.
    
    Prevention: Ergonomic workplace setup, regular hand and wrist stretches.
    
    Cure: Treatment includes rest, wrist splints, anti-inflammatory medications, and sometimes surgery to relieve pressure on the median nerve.
    
    """,
        """
    Disease: Chickenpox
    
    Description: Chickenpox is a highly contagious viral infection characterized by an itchy rash of red spots and blisters.
    
    Causes: Varicella-zoster virus.
    
    Symptoms: Itchy rash, fever, fatigue, and in severe cases, complications like pneumonia and encephalitis.
    
    Prevention: Vaccination (varicella vaccine) is the most effective prevention method.
    
    Cure: Chickenpox usually resolves on its own within a few weeks. Symptomatic treatment and avoiding scratching are important to prevent secondary infections.
    
    """,
        """
    Disease: Cleft Lip and Palate
    
    Description: Cleft lip and palate are congenital conditions where there's a gap or opening in the upper lip and/or the roof of the mouth.
    
    Causes: A combination of genetic and environmental factors during pregnancy.
    
    Symptoms: Visible gap or opening in the lip and/or palate, feeding difficulties in infants.
    
    Prevention: There's no surefire prevention, but managing risk factors like smoking during pregnancy can reduce the risk.
    
    Cure: Surgical repair is the primary treatment, often performed in stages during childhood. Speech therapy and other interventions may be needed.
    
    """,
        """
    Disease: Clubfoot
    
    Description: Clubfoot is a congenital condition where a baby's foot is turned inward and downward, making it difficult to walk normally.
    
    Causes: The exact cause is often unknown but may involve genetic and environmental factors.
    
    Symptoms: Foot turned inward and downward, limited movement in the ankle and foot.
    
    Prevention: There's no prevention, but early diagnosis and treatment are important.
    
    Cure: Treatment involves gentle manipulation, casting, and sometimes surgery to correct the foot's position and allow normal development.
    
    """,
        """
    Disease: Congestive Heart Failure
    
    Description: Congestive heart failure is a chronic condition where the heart's ability to pump blood is compromised, leading to fluid buildup and organ dysfunction.
    
    Causes: Conditions like coronary artery disease, high blood pressure, and heart valve disorders.
    
    Symptoms: Shortness of breath, fatigue, swelling in the legs, rapid heartbeat.
    
    Prevention: Managing risk factors like high blood pressure, diabetes, and maintaining a healthy lifestyle.
    
    Cure: While there's no cure, treatment involves medications, lifestyle changes, and in severe cases, heart transplantation.
    
    """,
        """
    Disease: Cryptosporidiosis
    
    Description: Cryptosporidiosis is a parasitic infection that causes gastrointestinal symptoms, often associated with contaminated water or food.
    
    Causes: Cryptosporidium parasites.
    
    Symptoms: Diarrhea, stomach cramps, nausea, vomiting, and fever.
    
    Prevention: Drinking clean and safe water, practicing good hygiene, and avoiding consumption of contaminated food.
    
    Cure: Treatment is mainly supportive, focusing on managing symptoms. In healthy individuals, the infection typically resolves on its own.
    
    """,

        """
    Disease: Diphtheria
    
    Description: Diphtheria is a bacterial infection that affects the respiratory tract, causing a thick gray coating in the throat and potentially leading to severe complications.
    
    Causes: Corynebacterium diphtheriae bacteria.
    
    Symptoms: Sore throat, fever, difficulty breathing, and the characteristic gray coating in the throat.
    
    Prevention: Vaccination (diphtheria-tetanus-pertussis vaccine) is highly effective.
    
    Cure: Treatment involves antibiotics and antitoxin. Diphtheria can be fatal if left untreated.
    
    """,
        """
    Disease: Down Syndrome
    
    Description: Down syndrome is a genetic disorder caused by the presence of an extra copy of chromosome 21, leading to intellectual and developmental challenges.
    
    Causes: Trisomy 21, a genetic abnormality where there's an extra copy of chromosome 21.
    
    Symptoms: Intellectual and developmental delays, distinct facial features, and potential health complications.
    
    Prevention: Down syndrome cannot be prevented, as it's a genetic condition.
    
    Cure: There's no cure, but early interventions, therapies, and medical care can help individuals with Down syndrome reach their full potential.
    
    """,
        """
    Disease: Dysentery
    
    Description: Dysentery is a gastrointestinal infection that causes severe diarrhea with blood or mucus, along with abdominal cramps and fever.
    
    Causes: Bacterial (Shigella, Salmonella), viral, or parasitic infections.
    
    Symptoms: Severe diarrhea with blood or mucus, abdominal cramps, fever, and dehydration.
    
    Prevention: Practicing good hygiene, clean water consumption, and safe food handling.
    
    Cure: Treatment focuses on addressing dehydration and managing symptoms through oral rehydration and, in some cases, medications.
    
    """,
        """
    Disease: E. Coli Infection
    
    Description: E. coli infections can range from mild stomach upset to severe illness, especially when a specific strain (E. coli O157:H7) is involved.
    
    Causes: Consumption of contaminated food, water, or contact with infected animals.
    
    Symptoms: Stomach cramps, diarrhea (often bloody), vomiting, and fever.
    
    Prevention: Safe food handling, avoiding consumption of undercooked ground beef, and practicing good hygiene.
    
    Cure: Most E. coli infections resolve on their own. Severe cases may require medical attention and monitoring.
    
    """,
        """
    Disease: Eczema
    
    Description: Eczema, or atopic dermatitis, is a chronic skin condition characterized by itchy, inflamed skin.
    
    Causes: Complex interplay of genetic and environmental factors.
    
    Symptoms: Itchy, red, and inflamed skin patches, which can lead to scratching and further complications.
    
    Prevention: Managing triggers like allergens, using gentle skincare products, and moisturizing regularly.
    
    Cure: There's no cure, but treatment involves managing symptoms through moisturizers, topical corticosteroids, and lifestyle changes.
    
    """,
        """
    Disease: Embolic Stroke
    
    Description: Embolic stroke occurs when a blood clot (embolus) travels from elsewhere in the body and blocks an artery in the brain.
    
    Causes: Blood clots originating from the heart or other arteries.
    
    Symptoms: Sudden weakness, numbness, or paralysis of the face, arm, or leg, along with speech difficulties and confusion.
    
    Prevention: Managing risk factors like high blood pressure, diabetes, and maintaining a healthy lifestyle.
    
    Cure: Treatment involves restoring blood flow, often through medications or surgical interventions. Stroke rehabilitation is important for recovery.
    
    """,
        """
    Disease: Encephalitis
    
    Description: Encephalitis is the inflammation of the brain, often caused by viral infections and leading to neurological symptoms.
    
    Causes: Viral infections, such as herpes simplex virus or arboviruses transmitted by mosquitoes.
    
    Symptoms: Headache, fever, confusion, seizures, and in severe cases, altered consciousness.
    
    Prevention: Vaccination (if available), mosquito control in areas prone to arbovirus transmission.
    
    Cure: Treatment focuses on managing symptoms and addressing the underlying cause. In severe cases, hospitalization and supportive care may be necessary.
    
    """,
        """
    Disease: Enterovirus
    
    Description: Enteroviruses are a group of viruses that can cause a range of symptoms, from mild cold-like symptoms to more severe illnesses.
    
    Causes: Various enteroviruses, including coxsackieviruses and echoviruses.
    
    Symptoms: Mild respiratory or gastrointestinal symptoms, and in some cases, more severe illnesses like meningitis or encephalitis.
    
    Prevention: Practicing good hygiene, especially handwashing.
    
    Cure: Treatment focuses on managing symptoms, and most cases resolve on their own.
    
    """,
        """
    Disease: Fibroids
    
    Description: Fibroids are non-cancerous growths that form in or on the uterus, leading to symptoms like heavy menstrual bleeding and pelvic pain.
    
    Causes: The exact cause is unclear, but hormonal factors and genetics may play a role.
    
    Symptoms: Heavy menstrual bleeding, pelvic pain, frequent urination, and pressure on the pelvis.
    
    Prevention: There's no surefire prevention, but maintaining a healthy weight and managing hormonal imbalances may help.
    
    Cure: Treatment options range from medication to surgical procedures, depending on the size and severity of the fibroids.
    
    """,
        """
    Disease: Foot and Mouth Disease
    
    Description: Foot and mouth disease is a highly contagious viral infection affecting cloven-hoofed animals, causing blisters on the mouth, hooves, and udder.
    
    Causes: Foot and mouth disease virus.
    
    Symptoms: Blisters and sores on the mouth, hooves, and udder of affected animals, along with fever.
    
    Prevention: Vaccination, biosecurity measures, and proper quarantine of infected animals.
    
    Cure: Infected animals may recover on their own, but the disease can have economic impacts due to reduced meat and milk production.
    
    """,

        """
    Disease: Guillain-Barré Syndrome
    
    Description: Guillain-Barré syndrome is a rare neurological disorder where the body's immune system attacks the peripheral nervous system, leading to muscle weakness and sometimes paralysis.
    
    Causes: Often triggered by infections, particularly viral or bacterial infections.
    
    Symptoms: Muscle weakness, tingling, and in severe cases, paralysis. Symptoms may start in the legs and progress upward.
    
    Prevention: There's no known way to prevent Guillain-Barré syndrome.
    
    Cure: Treatment focuses on supportive care, including physical therapy and sometimes immunoglobulin therapy or plasmapheresis.
    
    """,
        """
    Disease: Hashimoto's Thyroiditis
    
    Description: Hashimoto's thyroiditis is an autoimmune disorder that leads to inflammation of the thyroid gland, causing hypothyroidism.
    
    Causes: The immune system mistakenly attacks the thyroid gland.
    
    Symptoms: Fatigue, weight gain, depression, and other symptoms of hypothyroidism.
    
    Prevention: There's no known prevention for Hashimoto's thyroiditis.
    
    Cure: Treatment involves hormone replacement therapy to manage hypothyroidism and reduce symptoms.
    
    """,
        """
    Disease: Hemorrhoids
    
    Description: Hemorrhoids are swollen and inflamed veins in the lower rectum or anus, causing discomfort and pain.
    
    Causes: Straining during bowel movements, chronic constipation, pregnancy, and obesity.
    
    Symptoms: Pain, itching, and bleeding during bowel movements.
    
    Prevention: Maintaining regular bowel habits, avoiding straining, and consuming a high-fiber diet.
    
    Cure: Treatment involves lifestyle changes, topical creams, and in severe cases, procedures to remove or shrink hemorrhoids.
    
    """,
        """
    Disease: Hepatitis A
    
    Description: Hepatitis A is a contagious viral infection affecting the liver and causing flu-like symptoms, jaundice, and liver inflammation.
    
    Causes: Hepatitis A virus transmitted through contaminated food, water, or close contact.
    
    Symptoms: Fatigue, fever, jaundice, dark urine, and abdominal pain.
    
    Prevention: Vaccination (hepatitis A vaccine), practicing good hygiene, and avoiding contaminated food and water.
    
    Cure: Most people recover fully without treatment, but supportive care is important. In severe cases, hospitalization may be necessary.
    
    """,
        """
    Disease: Hepatitis B
    
    Description: Hepatitis B is a viral infection affecting the liver, with acute and chronic forms that can lead to serious liver damage.
    
    Causes: Hepatitis B virus transmitted through blood, sexual contact, and from mother to child during childbirth.
    
    Symptoms: Fatigue, jaundice, abdominal pain, and flu-like symptoms.
    
    Prevention: Vaccination (hepatitis B vaccine), safe sex practices, and avoiding sharing needles or personal items.
    
    Cure: Acute hepatitis B infections may resolve on their own, while chronic infections may require antiviral medications and monitoring.
    
    """,
        """
    Disease: Herpes Simplex Virus (HSV)
    
    Description: HSV is a common viral infection causing oral herpes (cold sores) or genital herpes, with periodic outbreaks.
    
    Causes: Herpes simplex virus type 1 (oral herpes) and type 2 (genital herpes).
    
    Symptoms: Painful sores or blisters on or around the mouth (oral herpes) or genital area (genital herpes).
    
    Prevention: Practicing safe sex and avoiding contact with active sores.
    
    Cure: There's no cure, but antiviral medications can shorten outbreaks and reduce symptoms.
    
    """,
        """
    Disease: Hypothyroidism
    
    Description: Hypothyroidism is a condition where the thyroid gland doesn't produce enough thyroid hormones, leading to various health issues.
    
    Causes: Autoimmune disorders, thyroid surgery, and certain medications.
    
    Symptoms: Fatigue, weight gain, cold sensitivity, depression, and dry skin.
    
    Prevention: There's no known prevention for hypothyroidism.
    
    Cure: Treatment involves hormone replacement therapy to restore thyroid hormone levels and manage symptoms.
    
    """,
        """
    Disease: Impetigo
    
    Description: Impetigo is a contagious bacterial skin infection causing red sores that can break open and develop a yellow-brown crust.
    
    Causes: Staphylococcus aureus or Streptococcus pyogenes bacteria.
    
    Symptoms: Red sores, blisters, or pustules that break open and form a crust.
    
    Prevention: Practicing good hygiene and avoiding close contact with infected individuals.
    
    Cure: Treatment involves topical antibiotics for mild cases and oral antibiotics for more severe cases.
    
    """,
        """
    Disease: Inflammatory Bowel Disease (IBD)
    
    Description: IBD is a group of chronic disorders causing inflammation in the digestive tract, including Crohn's disease and ulcerative colitis.
    
    Causes: Complex interplay of genetics, immune system dysfunction, and environmental factors.
    
    Symptoms: Abdominal pain, diarrhea, fatigue, weight loss, and in severe cases, complications affecting other organs.
    
    Prevention: There's no known prevention, but managing stress and maintaining a healthy lifestyle can help.
    
    Cure: There's no cure, but treatment involves managing symptoms through medications, dietary changes, and sometimes surgery.
    
    """,
        """
    Disease: Interstitial Cystitis
    
    Description: Interstitial cystitis (IC) is a chronic bladder condition causing bladder pain, urgency, and frequency of urination.
    
    Causes: The exact cause is unknown but may involve a combination of factors.
    
    Symptoms: Bladder pain, frequent urination, and urgency.
    
    Prevention: There's no known prevention for interstitial cystitis.
    
    Cure: Treatment focuses on managing symptoms, including lifestyle changes, medications, and bladder training techniques.
    
    """,

        """
    Disease: Irritable Bowel Syndrome (IBS)
    
    Description: IBS is a common gastrointestinal disorder characterized by abdominal pain, bloating, and changes in bowel habits.
    
    Causes: The exact cause is unclear, but factors like diet, stress, and gut motility play a role.
    
    Symptoms: Abdominal pain, bloating, diarrhea, constipation, or alternating between both.
    
    Prevention: Managing stress, dietary modifications, and avoiding trigger foods.
    
    Cure: There's no cure, but lifestyle changes, dietary adjustments, and medications can help manage symptoms.
    
    """,
        """
    Disease: Jaundice
    
    Description: Jaundice is a yellowing of the skin and eyes due to an excess of bilirubin, a yellow pigment, in the bloodstream.
    
    Causes: Liver diseases, blocked bile ducts, or increased breakdown of red blood cells.
    
    Symptoms: Yellowing of the skin and eyes, dark urine, and pale stools.
    
    Prevention: Preventing underlying causes, such as managing liver disease or avoiding excessive alcohol consumption.
    
    Cure: Treatment involves addressing the underlying cause of jaundice, which may include medications, lifestyle changes, or medical procedures.
    
    """,
        """
    Disease: Kawasaki Disease
    
    Description: Kawasaki disease is a rare childhood illness that causes inflammation of blood vessels, mainly affecting young children.
    
    Causes: The cause is unknown, but it may involve an abnormal immune response to an infection.
    
    Symptoms: High fever, rash, redness and swelling of the hands and feet, swollen lymph nodes.
    
    Prevention: There's no known prevention for Kawasaki disease.
    
    Cure: Treatment involves intravenous immunoglobulin and aspirin to reduce inflammation and prevent complications.
    
    """,
        """
    Disease: Listeriosis
    
    Description: Listeriosis is a bacterial infection caused by consuming food contaminated with the bacterium Listeria monocytogenes.
    
    Causes: Consuming contaminated food, particularly unpasteurized dairy products, deli meats, and certain vegetables.
    
    Symptoms: Fever, muscle aches, nausea, and diarrhea.
    
    Prevention: Avoiding high-risk foods, practicing good hygiene, and cooking food thoroughly.
    
    Cure: Treatment involves antibiotics, especially for severe cases or infections in pregnant women.
    
    """,
        """
    Disease: Lymphoma
    
    Description: Lymphoma is a type of cancer that originates in the lymphocytes, a type of white blood cell involved in the immune system.
    
    Causes: Complex interplay of genetic and environmental factors.
    
    Symptoms: Enlarged lymph nodes, fatigue, fever, weight loss, and night sweats.
    
    Prevention: There's no known prevention for lymphoma.
    
    Cure: Treatment varies based on the type and stage of lymphoma, including chemotherapy, radiation, targeted therapies, and stem cell transplantation.
    
    """,
        """
    Disease: Macular Degeneration
    
    Description: Macular degeneration is a progressive eye condition that affects the central part of the retina, leading to vision loss.
    
    Causes: Age-related changes and genetic factors.
    
    Symptoms: Blurred or distorted central vision, difficulty reading or recognizing faces.
    
    Prevention: Protecting eyes from UV light, maintaining a healthy lifestyle, and managing risk factors like high blood pressure and smoking.
    
    Cure: There's no cure, but treatment may include medications, laser therapy, and vision aids to manage symptoms.
    
    """,
        """
    Disease: Menopause
    
    Description: Menopause is a natural biological process in women that marks the end of reproductive years, resulting in hormonal changes and the cessation of menstruation.
    
    Causes: Natural decline in reproductive hormones, particularly estrogen.
    
    Symptoms: Irregular periods, hot flashes, night sweats, mood changes, and vaginal dryness.
    
    Prevention: There's no prevention, as menopause is a natural process.
    
    Cure: There's no cure, but hormone therapy, lifestyle changes, and symptom management can improve quality of life.
    
    """,
        """
    Disease: Menstrual Disorders
    
    Description: Menstrual disorders encompass a range of conditions affecting the menstrual cycle, including heavy periods, irregular periods, and painful periods.
    
    Causes: Hormonal imbalances, underlying health conditions, and genetic factors.
    
    Symptoms: Vary based on the specific disorder but may include heavy bleeding, irregular cycles, and severe cramps.
    
    Prevention: Maintaining a healthy lifestyle and managing underlying health conditions.
    
    Cure: Treatment depends on the specific disorder and may involve hormonal therapies, lifestyle changes, and medications.
    
    """,
        """
    Disease: Myasthenia Gravis
    
    Description: Myasthenia gravis is a neuromuscular disorder causing muscle weakness and fatigue, often worsened with activity.
    
    Causes: Autoimmune disorder where the immune system attacks receptors on muscle cells.
    
    Symptoms: Muscle weakness, particularly in the face, neck, and limbs.
    
    Prevention: There's no known prevention for myasthenia gravis.
    
    Cure: While there's no cure, treatment involves medications to improve muscle function and manage symptoms.
    
    """,
        """
    Disease: Narcolepsy
    
    Description: Narcolepsy is a chronic neurological disorder causing excessive daytime sleepiness and sudden sleep attacks.
    
    Causes: The exact cause is unknown, but genetics and autoimmune factors may play a role.
    
    Symptoms: Excessive daytime sleepiness, sudden loss of muscle tone (cataplexy), sleep paralysis, and hallucinations.
    
    Prevention: There's no known prevention for narcolepsy.
    
    Cure: Treatment includes medications to manage symptoms, lifestyle adjustments, and sleep hygiene practices.
    
    """,

        """
    Disease: Cataracts
    
    Description: Cataracts are a common age-related eye condition where the normally clear lens of the eye becomes cloudy, leading to blurred or decreased vision.
    
    Causes: The primary cause of cataracts is aging, but factors like UV radiation, smoking, diabetes, and certain medications can increase the risk.
    
    Symptoms: Blurred, cloudy, or dim vision, sensitivity to light, difficulty seeing at night, and needing brighter light for reading and other activities.
    
    Prevention: Protecting your eyes from UV light, quitting smoking, managing diabetes, and having regular eye checkups.
    
    Cure: Cataracts can be treated with surgery to remove the cloudy lens and replace it with an artificial lens.
    
    """,
        """
    Disease: Ovarian Cysts
    
    Description: Ovarian cysts are fluid-filled sacs that can develop on the ovaries, often causing pain, discomfort, and changes in the menstrual cycle.
    
    Causes: Ovarian cysts can result from the normal menstrual cycle, hormonal imbalances, or conditions like polycystic ovary syndrome (PCOS).
    
    Symptoms: Pelvic pain, bloating, swelling, changes in menstrual patterns, and pain during intercourse.
    
    Prevention: Maintaining a healthy lifestyle and managing conditions like PCOS that increase the risk of cysts.
    
    Cure: Most ovarian cysts resolve on their own. Treatment may be needed if cysts are large, causing pain, or if they don't go away on their own.
    
    """,
        """
    Disease: Restless Legs Syndrome
    
    Description: Restless legs syndrome (RLS) is a neurological disorder characterized by an uncontrollable urge to move the legs, often accompanied by uncomfortable sensations.
    
    Causes: The exact cause is unclear, but genetic factors, dopamine imbalance, and certain medical conditions can contribute.
    
    Symptoms: Uncomfortable sensations in the legs, particularly at rest, leading to an irresistible urge to move.
    
    Prevention: Managing triggers like caffeine and nicotine, maintaining a regular sleep schedule, and practicing relaxation techniques.
    
    Cure: While there's no cure, RLS can be managed with medications, lifestyle changes, and addressing underlying conditions.
    
    """,
        """
    Disease: Sleep Apnea
    
    Description: Sleep apnea is a sleep disorder where breathing repeatedly stops and starts during sleep, leading to poor sleep quality, daytime sleepiness, and other health issues.
    
    Causes: Obstructive sleep apnea occurs when the muscles in the throat relax too much, central sleep apnea results from a signaling problem in the brain.
    
    Symptoms: Loud snoring, choking or gasping during sleep, excessive daytime sleepiness, and difficulty concentrating.
    
    Prevention: Maintaining a healthy weight, avoiding alcohol and sedatives before sleep, and sleeping on your side.
    
    Cure: Treatment options include lifestyle changes, CPAP therapy, oral appliances, and surgery for severe cases.
    
    """,
        """
    Disease: Stomach Ulcers
    
    Description: Stomach ulcers, also known as peptic ulcers, are open sores that form on the lining of the stomach, small intestine, or esophagus.
    
    Causes: Most stomach ulcers are caused by H. pylori infection, NSAIDs, and lifestyle factors like stress and smoking.
    
    Symptoms: Burning stomach pain, bloating, belching, nausea, vomiting, and unintended weight loss.
    
    Prevention: Avoiding NSAIDs, managing stress, and treating H. pylori infection.
    
    Cure: Treatment involves medications to reduce stomach acid, antibiotics for H. pylori, and lifestyle changes to promote healing.
    
    """,
        """
    Disease: Thyroid Disorders
    
    Description: Thyroid disorders involve abnormal functioning of the thyroid gland, affecting the production of thyroid hormones essential for various bodily functions.
    
    Causes: Thyroid disorders can result from autoimmune diseases, iodine deficiency, genetics, and other factors.
    
    Symptoms: Vary based on the specific disorder but may include weight changes, fatigue, temperature sensitivity, and mood swings.
    
    Prevention: Consuming iodized salt to prevent iodine deficiency-related thyroid disorders.
    
    Cure: Treatment depends on the specific disorder and may involve medication, radioactive iodine therapy, or surgery.
    
    """,
        """
    Disease: Urinary Tract Infections (UTIs)
    
    Description: UTIs are infections that occur anywhere in the urinary system, including the bladder, urethra, and kidneys.
    
    Causes: Most UTIs are caused by bacteria entering the urinary tract through the urethra.
    
    Symptoms: Frequent and painful urination, cloudy or bloody urine, lower abdominal pain, and a strong urge to urinate.
    
    Prevention: Drinking plenty of water, urinating after sexual intercourse, and practicing good hygiene.
    
    Cure: UTIs are treated with antibiotics to clear the infection. Severe cases or kidney infections may require hospitalization.
    
    """,
        """
    Disease: Varicose Veins
    
    Description: Varicose veins are swollen and twisted veins that are visible under the skin, often occurring in the legs and causing discomfort.
    
    Causes: Weakened vein walls and valves, genetic predisposition, pregnancy, and prolonged standing.
    
    Symptoms: Enlarged, twisted veins that may appear blue or dark purple and cause pain, aching, and itching.
    
    Prevention: Regular exercise, maintaining a healthy weight, elevating the legs, and avoiding prolonged standing.
    
    Cure: Treatment options include lifestyle changes, compression stockings, and medical procedures like vein ablation or stripping.
    
    """,
        """
    Disease: Whooping Cough (Pertussis)
    
    Description: Whooping cough, also known as pertussis, is a highly contagious bacterial infection that causes severe coughing fits and a "whooping" sound.
    
    Causes: Bordetella pertussis bacteria, spread through respiratory droplets.
    
    Symptoms: Initially resemble a cold, followed by severe coughing fits, and a distinctive "whooping" sound during inhalation.
    
    Prevention: Vaccination (DTaP or Tdap vaccines) for children, adolescents, and adults, and booster shots as recommended.
    
    Cure: Treatment involves antibiotics to shorten the duration of symptoms and reduce transmission. Prevention through vaccination is crucial.
    
    """,
        """
    Disease: Yellow Fever
    
    Description: Yellow fever is a viral disease transmitted by infected mosquitoes, causing flu-like symptoms, jaundice, and potentially fatal complications.
    
    Causes: Yellow fever virus transmitted by Aedes mosquitoes in tropical and subtropical regions.
    
    Symptoms: Sudden onset of fever, chills, severe headache, muscle aches, and jaundice.
    
    Prevention: Vaccination (yellow fever vaccine) and mosquito bite prevention measures.
    
    Cure: There's no specific antiviral treatment for yellow fever. Supportive care and managing symptoms are essential.
    
    """,
        """
    Disease: Typhoid
    
    Description: Typhoid is a bacterial infection caused by Salmonella typhi bacteria, leading to high fever, abdominal pain, and gastrointestinal symptoms.
    
    Causes: Contaminated food, water, or close contact with infected individuals.
    
    Symptoms: High fever, abdominal pain, headache, diarrhea or constipation, and rose-colored spots on the chest.
    
    Prevention: Drinking safe water, practicing good hygiene, and getting vaccinated (typhoid vaccine).
    
    Cure: Treatment involves antibiotics to clear the infection. Prevention through safe food and water practices is crucial.
    
    """,

        """
    Disease: Zika Virus
    
    Description: Zika virus is a mosquito-borne viral infection that can cause mild symptoms in some, but it can lead to severe birth defects if contracted during pregnancy.
    
    Causes: Spread through Aedes mosquitoes primarily and can also be transmitted through sexual contact.
    
    Symptoms: Fever, rash, joint pain, conjunctivitis (red eyes), and muscle pain.
    
    Prevention: Preventing mosquito bites, safe sexual practices, and avoiding travel to Zika-affected areas, especially for pregnant women.
    
    Cure: There's no specific treatment, but supportive care is recommended for managing symptoms. Pregnant women should avoid Zika exposure.
    
    """,
        """
    Disease: Anorexia Nervosa
    
    Description: Anorexia nervosa is an eating disorder characterized by an intense fear of gaining weight, leading to self-imposed starvation and excessive weight loss.
    
    Causes: Complex interplay of genetic, psychological, and environmental factors.
    
    Symptoms: Extreme weight loss, obsession with food, distorted body image, and denial of hunger.
    
    Prevention: Early intervention, promoting positive body image, and fostering healthy attitudes toward food.
    
    Cure: Treatment involves psychotherapy, nutritional counseling, medical monitoring, and addressing underlying psychological issues.
    
    """,
        """
    Disease: Binge Eating Disorder
    
    Description: Binge eating disorder is an eating disorder characterized by recurrent episodes of consuming large amounts of food in a short time, often leading to guilt and distress.
    
    Causes: Psychological factors, genetics, and environmental influences.
    
    Symptoms: Frequent episodes of excessive eating, feeling out of control, and eating even when not hungry.
    
    Prevention: Early intervention, psychological therapy, and addressing emotional triggers for overeating.
    
    Cure: Treatment involves psychotherapy, cognitive-behavioral therapy, and addressing emotional eating patterns.
    
    """,
        """
    Disease: Bulbar Palsy
    
    Description: Bulbar palsy is a motor neuron disease affecting the muscles involved in speech and swallowing due to damage to the brainstem.
    
    Causes: Neurodegenerative disorders like amyotrophic lateral sclerosis (ALS) and certain viral infections.
    
    Symptoms: Difficulty speaking, swallowing, and controlling facial muscles.
    
    Prevention: Varies based on the underlying cause; managing neurodegenerative conditions can help.
    
    Cure: There's no cure, but treatment focuses on symptom management, speech therapy, and supportive care.
    
    """,
        """
    Disease: Chronic Obstructive Pulmonary Disease (COPD)
    
    Description: COPD is a progressive lung disease that causes difficulty breathing due to airflow limitation, primarily from smoking or exposure to pollutants.
    
    Causes: Smoking, long-term exposure to lung irritants, and genetic factors.
    
    Symptoms: Shortness of breath, chronic cough, wheezing, and excess mucus production.
    
    Prevention: Avoiding smoking and exposure to lung irritants, early diagnosis, and managing lung health.
    
    Cure: There's no cure, but treatment involves managing symptoms, quitting smoking, medications, and pulmonary rehabilitation.
    
    """,
        """
    Disease: Deep Vein Thrombosis (DVT)
    
    Description: DVT is a blood clot that forms in a deep vein, often in the legs, and can be life-threatening if it dislodges and travels to the lungs (pulmonary embolism).
    
    Causes: Prolonged immobility, surgery, pregnancy, genetic factors, and certain medical conditions.
    
    Symptoms: Swelling, pain, warmth, and redness in the affected leg.
    
    Prevention: Staying active, avoiding prolonged sitting, and using compression stockings during long travel.
    
    Cure: Treatment includes anticoagulant medications to prevent clot growth and complications.
    
    """,
        """
    Disease: Emphysema
    
    Description: Emphysema is a type of COPD characterized by the destruction of the air sacs in the lungs, leading to difficulty exhaling and getting enough oxygen.
    
    Causes: Smoking, long-term exposure to lung irritants, and genetic factors.
    
    Symptoms: Shortness of breath, chronic cough, wheezing, and decreased exercise tolerance.
    
    Prevention: Avoiding smoking and exposure to lung irritants, early diagnosis, and managing lung health.
    
    Cure: There's no cure, but treatment involves managing symptoms, quitting smoking, medications, and pulmonary rehabilitation.
    
    """,
        """
    Disease: Fibrodysplasia Ossificans Progressiva (FOP)
    
    Description: FOP is a rare genetic disorder where soft tissues progressively turn into bone, restricting movement and causing disability.
    
    Causes: Genetic mutation leading to abnormal bone formation.
    
    Symptoms: Formation of bone in soft tissues, restricted movement, and flare-ups triggered by injury.
    
    Prevention: There's no known prevention for FOP.
    
    Cure: There's no cure, and treatment focuses on managing symptoms and complications.
    
    """,
        """
    Disease: Gaucher Disease
    
    Description: Gaucher disease is a rare genetic disorder where a fatty substance accumulates in cells, leading to a range of symptoms.
    
    Causes: Deficiency of the enzyme glucocerebrosidase.
    
    Symptoms: Enlarged liver and spleen, anemia, bone pain, and fatigue.
    
    Prevention: There's no known prevention for Gaucher disease.
    
    Cure: Enzyme replacement therapy and substrate reduction therapy are used to manage symptoms and slow disease progression.
    
    """,
        """
    Disease: Grave's Disease
    
    Description: Grave's disease is an autoimmune disorder causing the thyroid gland to overproduce thyroid hormones, leading to hyperthyroidism.
    
    Causes: Autoimmune response, genetic factors.
    
    Symptoms: Weight loss, rapid heart rate, bulging eyes, anxiety, and tremors.
    
    Prevention: There's no known prevention for Grave's disease.
    
    Cure: Treatment includes medications, radioactive iodine therapy, and surgery to manage hormone levels.
    
    """,

        """
    Disease: Acne
    
    Description: Acne is a common skin condition that occurs when hair follicles become clogged with oil and dead skin cells, leading to pimples, blackheads, and whiteheads.
    
    Causes: Overproduction of sebum (skin oil), hormonal changes, bacteria, and inflammation.
    
    Symptoms: Pimples, blackheads, whiteheads, and sometimes painful cysts on the face, back, and chest.
    
    Prevention: Good skincare practices, avoiding excessive scrubbing, and managing underlying hormonal imbalances.
    
    Cure: Treatment includes over-the-counter products, prescription medications, and in severe cases, dermatological procedures.
    
    """,
        """
    Disease: Anxiety Disorders
    
    Description: Anxiety disorders encompass various mental health conditions characterized by excessive worry, fear, and anxiety that interfere with daily life.
    
    Causes: Genetic predisposition, brain chemistry, and life experiences.
    
    Symptoms: Excessive worry, restlessness, irritability, and physical symptoms like rapid heartbeat and sweating.
    
    Prevention: Developing coping strategies, stress management, and seeking professional help.
    
    Cure: Treatment includes therapy (cognitive-behavioral therapy), medications, and lifestyle changes.
    
    """,
        """
    Disease: Bipolar Disorder
    
    Description: Bipolar disorder is a mood disorder characterized by alternating periods of manic (elevated mood) and depressive (low mood) episodes.
    
    Causes: Genetic factors, brain chemistry, and environmental triggers.
    
    Symptoms: Manic episodes (elevated mood, impulsive behavior) and depressive episodes (low mood, loss of interest).
    
    Prevention: Managing stress, maintaining a healthy routine, and seeking treatment.
    
    Cure: Treatment involves mood-stabilizing medications, therapy, and lifestyle adjustments.
    
    """,
        """
    Disease: Chronic Fatigue Syndrome (CFS)
    
    Description: CFS, also known as myalgic encephalomyelitis (ME), is a complex disorder characterized by extreme fatigue that doesn't improve with rest.
    
    Causes: The exact cause is unclear, possibly related to viral infections and immune system dysfunction.
    
    Symptoms: Persistent fatigue, cognitive difficulties, and unrefreshing sleep.
    
    Prevention: Managing stress, maintaining a balanced lifestyle, and pacing activities.
    
    Cure: Treatment focuses on symptom management, improving sleep, and adapting daily routines.
    
    """,
        """
    Disease: Cirrhosis
    
    Description: Cirrhosis is a late stage of scarring of the liver caused by long-term liver damage, leading to loss of liver function.
    
    Causes: Chronic alcohol abuse, viral hepatitis, and other conditions that damage the liver.
    
    Symptoms: Fatigue, easy bruising, swelling in the legs and abdomen, and confusion.
    
    Prevention: Limiting alcohol consumption, getting vaccinated for hepatitis, and managing underlying liver conditions.
    
    Cure: While there's no cure, treatment involves managing complications, lifestyle changes, and in some cases, liver transplantation.
    
    """,
        """
    Disease: Depression
    
    Description: Depression is a mood disorder characterized by persistent feelings of sadness, hopelessness, and a lack of interest or pleasure in activities.
    
    Causes: Genetic factors, brain chemistry, and life experiences.
    
    Symptoms: Persistent low mood, loss of interest, changes in appetite, and fatigue.
    
    Prevention: Maintaining a healthy lifestyle, managing stress, and seeking support.
    
    Cure: Treatment includes therapy (cognitive-behavioral therapy), medications, and lifestyle changes.
    
    """,
        """
    Disease: Gastroesophageal Reflux Disease (GERD)
    
    Description: GERD is a chronic condition where stomach acid flows back into the esophagus, causing symptoms like heartburn and acid regurgitation.
    
    Causes: Weakened lower esophageal sphincter, obesity, and certain foods.
    
    Symptoms: Heartburn, acid regurgitation, chest pain, and difficulty swallowing.
    
    Prevention: Avoiding trigger foods, eating smaller meals, and maintaining a healthy weight.
    
    Cure: Treatment includes lifestyle changes, medications to reduce acid production, and in severe cases, surgery.
    
    """,
        """
    Disease: Hemorrhagic Fever with Renal Syndrome (HFRS)
    
    Description: HFRS is a group of viral infections characterized by fever, kidney dysfunction, and bleeding tendencies.
    
    Causes: Hantaviruses transmitted by rodents, particularly through contact with their droppings or urine.
    
    Symptoms: Fever, chills, headache, abdominal pain, and kidney dysfunction.
    
    Prevention: Avoiding contact with rodents and their habitats, practicing good hygiene.
    
    Cure: Treatment focuses on managing symptoms, providing supportive care, and preventing complications.
    
    """,
        """
    Disease: Hypoglycemia
    
    Description: Hypoglycemia is a condition characterized by low blood sugar levels, often causing symptoms like shakiness, sweating, and confusion.
    
    Causes: Skipping meals, excessive insulin or diabetes medications, and certain medical conditions.
    
    Symptoms: Shakiness, sweating, rapid heartbeat, and confusion.
    
    Prevention: Maintaining balanced meals, monitoring blood sugar levels, and adjusting medications as needed.
    
    Cure: Treatment involves consuming a source of glucose to raise blood sugar levels quickly.
    
    """,
        """
    Disease: Inflammatory Bowel Disease (IBD)
    
    Description: IBD is a group of chronic inflammatory conditions affecting the digestive tract, including Crohn's disease and ulcerative colitis.
    
    Causes: Complex interplay of genetic, immune, and environmental factors.
    
    Symptoms: Abdominal pain, diarrhea, fatigue, and weight loss.
    
    Prevention: Managing stress, maintaining a balanced diet, and avoiding tobacco.
    
    Cure: While there's no cure, treatment focuses on managing symptoms, reducing inflammation, and preventing complications.
    
    """,

        """
    Disease: Leishmaniasis
    
    Description: Leishmaniasis is a parasitic disease transmitted by sandfly bites, causing skin sores and potentially affecting internal organs.
    
    Causes: Parasitic infection from Leishmania species.
    
    Symptoms: Skin sores, fever, weight loss, and enlarged spleen and liver in severe cases.
    
    Prevention: Avoiding sandfly bites, using insect repellents, and controlling sandfly populations.
    
    Cure: Treatment varies based on the type of leishmaniasis and may include antiparasitic medications.
    
    """,
        """
    Disease: Listeriosis
    
    Description: Listeriosis is a bacterial infection caused by consuming contaminated foods, often leading to flu-like symptoms and severe complications.
    
    Causes: Listeria monocytogenes bacteria found in contaminated food.
    
    Symptoms: Fever, muscle aches, nausea, diarrhea, and sometimes serious complications in vulnerable individuals.
    
    Prevention: Practicing good food hygiene, avoiding high-risk foods, and cooking foods thoroughly.
    
    Cure: Antibiotics are used to treat severe cases of listeriosis.
    
    """,
        """
    Disease: Lyme Disease
    
    Description: Lyme disease is a tick-borne infection caused by Borrelia burgdorferi bacteria, leading to a range of symptoms.
    
    Causes: Tick bites from infected black-legged ticks.
    
    Symptoms: Rash resembling a bull's-eye, fever, fatigue, joint pain, and neurological symptoms.
    
    Prevention: Avoiding tick exposure, using tick repellents, and wearing protective clothing.
    
    Cure: Antibiotics are used to treat Lyme disease in its early stages.
    
    """,
        """
    Disease: Marfan Syndrome
    
    Description: Marfan syndrome is a genetic disorder that affects the body's connective tissues, leading to various physical and health issues.
    
    Causes: Genetic mutation in the fibrillin-1 gene.
    
    Symptoms: Tall stature, long limbs, joint hypermobility, and cardiovascular complications.
    
    Prevention: Genetic counseling for individuals with a family history of Marfan syndrome.
    
    Cure: Treatment involves managing symptoms, addressing cardiovascular issues, and regular medical follow-up.
    
    """,
        """
    Disease: Migraine
    
    Description: Migraine is a neurological disorder characterized by recurrent, severe headaches often accompanied by sensory disturbances.
    
    Causes: Genetic predisposition, triggers like certain foods, hormonal changes, and stress.
    
    Symptoms: Throbbing headache, sensitivity to light and sound, and sometimes aura (visual disturbances).
    
    Prevention: Identifying and avoiding triggers, managing stress, and maintaining a consistent routine.
    
    Cure: Treatment includes pain relief medications, preventive medications, and lifestyle changes.
    
    """,
        """
    Disease: Obsessive-Compulsive Disorder (OCD)
    
    Description: OCD is a mental health disorder characterized by unwanted repetitive thoughts (obsessions) and behaviors (compulsions).
    
    Causes: Genetics, brain chemistry, and life experiences.
    
    Symptoms: Intrusive thoughts, repetitive behaviors, and a strong urge to perform compulsions.
    
    Prevention: Early intervention, psychotherapy, and medications.
    
    Cure: Treatment includes cognitive-behavioral therapy, exposure therapy, and sometimes medications.
    
    """,
        """
    Disease: Panic Disorder
    
    Description: Panic disorder is a type of anxiety disorder characterized by recurring panic attacks, sudden episodes of intense fear.
    
    Causes: Genetic factors, brain chemistry, and stress.
    
    Symptoms: Sudden intense fear, heart palpitations, sweating, and a feeling of impending doom.
    
    Prevention: Stress management, relaxation techniques, and seeking professional help.
    
    Cure: Treatment includes therapy (cognitive-behavioral therapy), medications, and lifestyle changes.
    
    """,
        """
    Disease: Post-Traumatic Stress Disorder (PTSD)
    
    Description: PTSD is a mental health disorder that can develop after experiencing or witnessing a traumatic event, causing distressing symptoms.
    
    Causes: Traumatic experiences, such as war, accidents, or assaults.
    
    Symptoms: Flashbacks, nightmares, hypervigilance, and emotional numbness.
    
    Prevention: Trauma-informed care, early intervention, and social support.
    
    Cure: Treatment includes therapy (cognitive-behavioral therapy), medications, and support groups.
    
    """,
        """
    Disease: Rheumatoid Arthritis
    
    Description: Rheumatoid arthritis is an autoimmune disorder causing joint inflammation, pain, and damage, often affecting multiple joints.
    
    Causes: Genetic factors, immune system dysfunction, and environmental triggers.
    
    Symptoms: Joint pain, stiffness, swelling, fatigue, and deformities.
    
    Prevention: Early diagnosis, medication management, and maintaining joint health.
    
    Cure: While there's no cure, treatment involves managing inflammation, pain, and joint damage.
    
    """,
        """
    Disease: Sarcoidosis
    
    Description: Sarcoidosis is an inflammatory disease that can affect multiple organs, leading to granulomas (abnormal tissue growth) and other symptoms.
    
    Causes: The exact cause is unclear, possibly involving genetics and immune system dysfunction.
    
    Symptoms: Fatigue, swollen lymph nodes, skin rashes, and respiratory symptoms.
    
    Prevention: Avoiding exposure to potential triggers and managing underlying conditions.
    
    Cure: Treatment focuses on managing symptoms, reducing inflammation, and preserving organ function.
    
    """,
        """
    Disease: Sepsis
    
    Description: Sepsis is a life-threatening response to infection where the body's own immune system causes widespread inflammation and organ dysfunction.
    
    Causes: Infection, often bacterial, that spreads to the bloodstream.
    
    Symptoms: Fever, rapid heart rate, confusion, low blood pressure, and organ dysfunction.
    
    Prevention: Preventing infections through good hygiene, vaccinations, and wound care.
    
    Cure: Sepsis requires immediate medical intervention in a hospital setting, including antibiotics and supportive care.
    
    """,
        """
    Disease: Systemic Lupus Erythematosus (SLE)
    
    Description: SLE is an autoimmune disease where the immune system attacks various body tissues, causing inflammation and a range of symptoms.
    
    Causes: Genetic factors, hormonal influences, and environmental triggers.
    
    Symptoms: Fatigue, joint pain, skin rashes, and inflammation affecting multiple organs.
    
    Prevention: Managing stress, maintaining a healthy lifestyle, and seeking early treatment.
    
    Cure: While there's no cure, treatment involves managing symptoms and preventing flare-ups.
    
    """,
        """
    Disease: Trichomoniasis
    
    Description: Trichomoniasis is a sexually transmitted infection (STI) caused by a parasite, often leading to vaginal or urethral discomfort.
    
    Causes: Infection with Trichomonas vaginalis parasite.
    
    Symptoms: Vaginal itching, burning, discharge, and discomfort during sex.
    
    Prevention: Practicing safe sex, using condoms, and avoiding sexual contact during treatment.
    
    Cure: Trichomoniasis is treated with prescription medications.
    
    """,
        """
    Disease: Tinnitus
    
    Description: Tinnitus is a perception of noise or ringing in the ears without any external sound source.
    
    Causes: Exposure to loud noise, age-related hearing loss, and other underlying conditions.
    
    Symptoms: Ringing, buzzing, or hissing sounds in the ears.
    
    Prevention: Protecting ears from loud noises, managing underlying conditions.
    
    Cure: While there's no cure, treatment focuses on managing symptoms and addressing underlying causes.
    
    """,
        """
    Disease: Uterine Fibroids
    
    Description: Uterine fibroids are noncancerous growths in the uterus that can cause pelvic pain and heavy menstrual bleeding.
    
    Causes: Hormonal and genetic factors.
    
    Symptoms: Pelvic pain, heavy or prolonged menstrual periods, and pressure on the bladder.
    
    Prevention: Healthy lifestyle, managing hormonal imbalances.
    
    Cure: Treatment options include medications, minimally invasive procedures, and surgery.
    
    """,
        """
    Disease: Wilson's Disease
    
    Description: Wilson's disease is a rare genetic disorder causing the accumulation of copper in the body, leading to liver and neurological problems.
    
    Causes: Genetic mutation affecting copper metabolism.
    
    Symptoms: Liver problems, neurological symptoms, and psychiatric disturbances.
    
    Prevention: Genetic counseling for individuals with a family history of Wilson's disease.
    
    Cure: Treatment involves medications to remove excess copper and manage symptoms.
    
    """,

        """
    Disease: Diarrhea
    
    Description: Diarrhea is a common digestive disorder characterized by frequent and loose bowel movements.
    
    Causes: Infections (bacterial, viral, or parasitic), dietary factors, medications, and underlying medical conditions.
    
    Symptoms: Frequent loose stools, abdominal cramps, and dehydration.
    
    Prevention: Practicing good hygiene, safe food preparation, staying hydrated, and avoiding food triggers.
    
    Cure: Treatment involves rehydration, dietary adjustments, and addressing underlying causes.
    
    """,
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',
    'dddddddddd',

]


preferred_keywords = ['anemia', 'als', 'celiac', 'compulsive', 'tinnitus', 'pancreatitis', 'obsessive-compulsive', "huntington's", 'hypoglycemia', 'renal', 'rabies', 'brucellosis', 'gout', 'hemophilia', 'kidney', 'cholera', 'bowel', 'copd', 'leprosy', 'apnea', 'osteoporosis', 'syndrome', 'gaucher', 'hepatitis', 'tract', 'ulcerative', 'degeneration', "wilson's", 'obsessive', "grave's", 'kawasaki', 'interstitial', 'irritable', 'disorder', 'thyroiditis', 'hiv/aids', 'chickenpox', 'post-traumatic', 'ebola', 'gonorrhea', 'chronic', 'parkinson', 'dengue', 'fibromyalgia', 'lupus', 'chikungunya', 'enterovirus', 'epilepsy', 'narcolepsy', 'menstrual', 'influenza', 'syphilis', "alzheimer's", 'hemorrhagic', 'yellow', 'arthritis', 'crohn', 'pertussis', 'tunnel', 'lyme', 'herpes', 'reflux', 'cancer', 'embolic', 'measles', 'leukemia', 'leishmaniasis', 'erythematosus', 'hypothyroidism', 'sclerosis', 'gastroesophageal', 'menopause', 'ibs', 'hfrs', 'uterine', 'gerd', 'myasthenia', 'gravis', 'simplex', 'alzheimer', 'zika', 'cystic', 'cataracts', 'osteoarthritis', 'encephalitis', 'dvt', 'bunions',
                      'sle', 'psoriasis', 'thrombosis', 'malaria', 'pneumonia', 'aids', 'lip', 'migraine', 'hiv', 'stroke', 'ibd', 'cirrhosis', 'esophagus', 'lung', 'sarcoidosis', 'depression', 'panic', 'vein', 'congestive', 'amyotrophic', 'ptsd', 'dysentery', 'bipolar', 'ulcers', 'cystitis', 'utis', 'heart', 'macular', 'marfan', 'chlamydia', 'fibrodysplasia', 'nervosa', 'asthma', 'hsv', 'ossificans', 'listeriosis', 'trichomoniasis', 'schizophrenia', 'impetigo', 'cysts', 'diphtheria', 'guillain-barré', 'pulmonary', 'disorders', 'bulbar', 'cfs', 'ulcer', 'fever', "parkinson's", 'sepsis', 'hemorrhoids', 'cryptosporidiosis', 'urinary', 'anorexia', 'infections', 'thyroid', 'lateral', 'colitis', 'restless', 'melanoma', 'down', 'typhoid', 'anxiety', 'sleep', 'fatigue', 'endometriosis', 'inflammatory', 'tuberculosis', 'emphysema', 'pneumothorax', 'traumatic', 'whooping', 'palate', 'failure', 'gastritis', 'diabetes', 'fibroids', 'clubfoot', 'fibrosis', 'hypertension', 'lymphoma', 'polio', 'binge', 'jaundice', 'palsy', 'sickle', 'acne', 'eczema', 'cough', 'huntington', 'ocd', 'glaucoma', 'ovarian']


greeting_queries = ['hello', 'can we talk' 'can you help', 'hi', 'how are you', 'hello, how are you' 'hi', 'how are you', 'hi there', 'hey', 'good morning', 'good afternoon', 'good evening', 'hi, how can i help you?', 'hello, what can i assist you with ?', 'hey, i have a question', 'hi! is there something you can help me with ?', 'greetings!', "hi, i'm looking for information", 'hi, can you provide some guidance?', 'hi, i need your expertise', "hello, i'm curious about something", "hi, i'm not sure where to start", 'hey, can you give me some advice?', "hi, i'm interested in learning more", 'hello, i hope you can assist me', "hi there, i'm seeking answers", 'hey, is this where i can get answers?', "hello, i hope you're here to help", 'hi, i need some information', "hey, i'm feeling a bit lost", "hello, i'm here with a question", 'hi, can you provide some insights?', "hey, i'm curious about something", "hello, i'm in search of answers", 'hi there, i need some assistance', "hey, i've got a query", "hello, i'm looking for guidance",
                    'hi, is there an expert i can talk to?', "hey, i'm hoping you can help me", 'hello, i need some clarification', "hi, i'm wondering about something", "hey, i'm seeking information", "hello, i'm hoping you can assist me", 'hi, i have a question for you', "hey, i'm not sure where to start", 'hello, i could use some advice', "hi, i'm hoping you're available", 'hey, can you provide some information?', "hello, i'm here to learn", 'hi, can you guide me?', "hey, i'm seeking your expertise", "hello, i've got a query for you", 'hi, can you shed some light?', "hey, i'm seeking some insights", "hello, i'm looking for answers", "hi, i hope you're here to help", 'hey, can you assist me?', "hello, i'm curious to know", 'hi, i need some information', "hey, i'm in need of assistance", "hello, i'm hoping you can guide me", "hi, i'm here with a question", "hey, i'm wondering about something", "hello, i'm seeking clarification", 'hi, i could use your expertise', 'hey, can you help me out?']


failed_queries = no_info_responses = [
    "I'm sorry, but I don't have any information about that.",
    "Unfortunately, I don't have the details you're looking for.",
    "I don't have any information on that particular topic.",
    "Regrettably, I cannot provide information on that subject.",
    "I apologize, but I lack information about that topic.",
    "I'm afraid I can't help you with that inquiry.",
    "I'm sorry, that topic is not within my knowledge base.",
    "Apologies, but I don't have any data on that subject.",
    "Unfortunately, I'm not equipped to answer that question.",
    "I'm sorry, but I don't have any relevant information.",
    "I regret to inform you that I don't have details on that topic.",
    "I'm sorry, I'm not able to provide insights on that matter.",
    "I don't have access to information about that particular subject.",
    "Regrettably, I can't offer any information on that topic.",
    "I apologize, but I don't possess knowledge about that topic."
]
