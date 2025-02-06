## List and Arrays
#%% Task One

MyList = ["Kuala Lumpur","London","Paris","New York","Bangkok"]

#Insert your code here

print(*MyList[1:4],sep="-")

#%% Task Two

MyList = ["Kuala Lumpur","London","Paris","New York","Bangkok"]

EnglishCity = "Oxford"
MyList.append(EnglishCity)
print(MyList)

MyList[1] = "Rome"
print(MyList)

MyList[-2] = "Tokyo"
print(MyList)



#%% Task Three

MyList = ["Kuala Lumpur","London","Paris","New York","Bangkok"]

for i in range(len(MyList)):
    print(i, MyList[i])



#%% Task Five
events = [["Queen Victoria's Funeral","February","1901","Marked the end of the Victorian era, Queen Victoria's funeral was a significant state affair that symbolized the end of her long reign. Her death was mourned globally, reflecting her widespread influence."],
["The Wright Brothers' First Flight","December","1903","Orville and Wilbur Wright achieved the first controlled and sustained flight of a powered airplane in Kitty Hawk, North Carolina. This event laid the foundation for modern aviation, transforming transportation."],
["Emily Davison Throws Herself Under The King's Derby Horse","June","1913","Emily Davison, a suffragette, made a dramatic protest for women's suffrage by throwing herself under King George V's horse at the Epsom Derby, becoming a poignant symbol of the suffrage movement."],
["Battle Of The Somme","July","1916","One of the bloodiest battles of World War I, the Battle of the Somme was marked by heavy casualties and is remembered for the use of trench warfare and the first use of tanks."],
["Abdication Of Tsar Nicholas","March","1917","Tsar Nicholas II of Russia abdicated his throne, leading to the end of the Romanov dynasty and paving the way for the Bolshevik Revolution."],
["Irish Free State Treaty Signed","December","1921","This treaty concluded the Irish War of Independence, establishing the Irish Free State and marking a significant step towards full Irish independence."],
["Suzanne Lenglen Breaks Wimbledon Record","July","1925","French tennis player Suzanne Lenglen dominated Wimbledon, setting records and becoming one of the first international female sports stars."],
["Start Of UK General Strike","May","1926","This was one of the largest industrial actions Britain ever saw, as workers protested in support of coal miners and against wage reductions and deteriorating working conditions."],
["Charles Lindbergh Flies The Atlantic Solo","May","1927","Charles Lindbergh made the first solo, nonstop transatlantic flight, flying from New York to Paris, which marked a major achievement in aviation history."],
["Wall Street Crash","October","1929","The Wall Street Crash of 1929, also known as the Great Crash, led to the Great Depression, affecting the global economy and causing widespread unemployment and hardship."],
["Hitler Becomes German Chancellor","January","1933","Adolf Hitler's appointment as Chancellor of Germany marked the beginning of the Third Reich, leading to WWII and the Holocaust."],
["Edward VIII Abdicates","December","1936","King Edward VIII abdicated the throne to marry Wallis Simpson, an American divorcee, leading to a constitutional crisis and the accession of King George VI."],
["Hindenburg Airship Crash","May","1937","The Hindenburg disaster was an airship crash in New Jersey, which marked the end of the use of airships in commercial transatlantic flight due to safety concerns."],
["Hitler Annexes Austria","March","1938","Adolf Hitler annexed Austria into Nazi Germany in an event known as the Anschluss, a critical step in the lead-up to World War II."],
["Germany Invades Poland","September","1939","The invasion of Poland by Germany sparked the beginning of World War II, leading to a global conflict that lasted until 1945."],
["Evacuation Of Dunkirk","May","1940","The evacuation, known as Operation Dynamo, saw the rescue of Allied soldiers from the beaches of Dunkirk, France, during World War II."],
["London Blitz Begins On Civilian Targets","September","1940","This was a major German bombing campaign against the United Kingdom during World War II, targeting many cities, predominantly London."],
["Pearl Harbour Attacked","December","1941","The surprise military strike by the Imperial Japanese Navy Air Service against the United States naval base at Pearl Harbor, Hawaii, led the U.S. to enter World War II."],
["Battle Of El Alamein Begins","October","1942","A turning point in the North African campaign of World War II, this battle marked the beginning of the end for the Axis powers in North Africa."],
["Fall Of Stalingrad - German Army Surrenders","January","1943","The Battle of Stalingrad was a major defeat for Nazi Germany, turning the tide in favor of the Allies on the Eastern Front during World War II."],
["D-Day Landings","June","1944","The Allied invasion of Normandy in Operation Overlord during World War II was the largest seaborne invasion in history and began the liberation of German-occupied France."],
["Liberation Of Paris","August","1944","This event marked the end of German occupation of Paris during World War II and was a significant step towards the Allied victory."],
["Big Three Meet At Yalta To Carve Up Post-War World","February","1945","Leaders of the Allied powers met at the Yalta Conference to discuss the post-war reorganization of Europe, significantly shaping the modern world."],
["Germans Surrender To Montgomery","May","1945","This marked the unconditional surrender of German forces to the Allies, leading to the end of World War II in Europe."],
["VE Day Celebrations","May","1945","Victory in Europe Day celebrated the formal acceptance by the Allies of World War II of Nazi Germany's unconditional surrender, marking the end of the war in Europe."],
["First Atomic Bomb Test In New Mexico","July","1945","Known as the Trinity test, this was the first detonation of a nuclear weapon, which marked the beginning of the atomic age."],
["Labour's Landslide Election Win","July","1945","The Labour Party won a landslide victory in the UK general election, leading to significant social reforms and the establishment of a welfare state."],
["Atomic Bomb Dropped On Hiroshima","August","1945","The United States dropped an atomic bomb on Hiroshima, Japan, the first use of nuclear weapons in warfare, leading to Japan's surrender and the end of World War II."],
["India And Pakistan Gain Independence","August","1947","The end of British rule in India led to the partition of India and Pakistan, resulting in one of the largest mass migrations in human history."],
["Berlin Airlift Begins","June","1948","In response to the Soviet blockade of West Berlin, the Western Allies organized the Berlin Airlift to deliver food and supplies, symbolizing Cold War tensions."],
["Mao's Communists Take Over In China","October","1949","Mao Zedong's Communist forces took control of mainland China, establishing the People's Republic of China and leading to significant geopolitical shifts."],
["Korean War Starts","June","1950","The invasion of South Korea by North Korea marked the beginning of the Korean War, a significant conflict in the Cold War era."],
["Britain Explodes First Atomic Bomb","October","1952","Britain conducted its first atomic bomb test, becoming the third country to independently develop and test nuclear weapons."],
["Launch Of First Nuclear Submarine","January","1954","The launch of USS Nautilus, the world's first operational nuclear-powered submarine, marked a new era in naval warfare."],
["Roger Bannister Breaks Four Minute Mile","May","1954","British athlete Roger Bannister became the first person to run a mile in under four minutes, a major milestone in athletics."],
["French Surrender At Dien Bien Phu","May","1954","This marked the end of French colonial rule in Indochina, leading to the independence of Vietnam, Laos, and Cambodia."],
["Le Mans 24 Race Disaster","June","1955","One of the worst accidents in motorsport history, a major crash during the 24 Hours of Le Mans race resulted in the deaths of over 80 spectators and a driver."],
["Khrushchev Denounces Stalin","February","1956","Soviet leader Nikita Khrushchev's denunciation of Joseph Stalin's reign marked the beginning of the 'de-Stalinization' process in the Soviet Union."],
["First Nuclear Power Station","October","1956","The world's first nuclear power station to generate electricity for a power grid started operating in Obninsk, USSR, marking a new era in energy production."],
["Soviets Crush Hungarian Revolt","November","1956","The Soviet Union forcefully suppressed the Hungarian Revolution, a nationwide revolt against the Marxist-Leninist government of the Hungarian People's Republic."],
["Suez Invasion","November","1956","The Suez Crisis of 1956 was a diplomatic and military confrontation involving Egypt, Israel, France, and the United Kingdom. The invasion by Israel followed by the UK and France aimed to regain Western control of the Suez Canal and remove Egyptian President Nasser. The crisis significantly strained relations between the West and the Arab world."],
["Manchester United Players Die In Munich Air Crash","February","1958","The Munich air disaster in February 1958 claimed the lives of 23 people, including players and staff of the Manchester United football team. The crash occurred as the team was returning from a European Cup match in Belgrade. This tragedy deeply affected Manchester United and the wider football community."],
["Pele's World Cup Final Performance Thrills Crowds","June","1958","In the 1958 FIFA World Cup, Pele, a 17-year-old Brazilian footballer, stunned the world with his extraordinary performance. He played a crucial role in Brazil's victory, showcasing remarkable skill and scoring two goals in the final. Pele's performance at this World Cup marked the beginning of his legendary career."],
["First Hovercraft Run","July","1959","The first successful hovercraft run in July 1959 marked a significant achievement in transportation technology. Invented by Christopher Cockerell, the hovercraft could travel over land, water, mud, and ice. This innovation opened up new possibilities for rapid and versatile transportation."],
["Kennedy Inauguration","January","1961","John F. Kennedy's inauguration as the 35th President of the United States took place in January 1961. His famous speech, where he stated, \"Ask not what your country can do for you—ask what you can do for your country,\" inspired a generation. Kennedy's presidency began with high hopes and ambition, symbolizing a new era in American politics."],
["Yuri Gagarin Becomes The First Man In Space","April","1961","Yuri Gagarin, a Soviet cosmonaut, became the first human to travel into space in April 1961. His spacecraft, Vostok 1, completed one orbit around the Earth. This historic event marked a significant milestone in the space race between the Soviet Union and the United States."],
["Erection Of The Berlin Wall","January","1961","The Berlin Wall, a symbol of the Cold War, was erected in August 1961 by the German Democratic Republic (East Germany). It was built to prevent East Germans from fleeing to West Berlin. The Wall stood until 1989 and was a stark symbol of the division between East and West."],
["Cuban Missile Crisis","October","1962","The Cuban Missile Crisis in October 1962 was a 13-day confrontation between the United States and the Soviet Union over Soviet ballistic missiles deployed in Cuba. It was the closest the Cold War came to escalating into a full-scale nuclear war. The crisis ended with an agreement to remove the missiles and is considered a turning point in the Cold War."],
["Martin Luther King Delivers His \"I Have A Dream\" Speech","August","1963","In August 1963, Martin Luther King Jr. delivered his iconic \"I Have a Dream\" speech during the March on Washington for Jobs and Freedom. His speech called for civil and economic rights and an end to racism in the United States. This event was a defining moment in the Civil Rights Movement."],
["Kennedy Assassinated","November","1963","President John F. Kennedy was assassinated in Dallas, Texas, in November 1963. His assassination shocked the world and led to widespread mourning and conspiracy theories. Kennedy's death marked a pivotal moment in American history and deeply affected the national psyche."],
["Beatles Return From States In Triumph","February","1964","In February 1964, The Beatles returned to the UK after their successful first visit to the United States. Their American tour marked the beginning of \"Beatlemania\" and the British Invasion in music. The Beatles' popularity in the US transformed the global music scene."],
["Aberfan Slag Heap Buries School","October","1966","In October 1966, a catastrophic collapse of a coal waste heap occurred in Aberfan, Wales, burying a primary school and killing 116 children and 28 adults. This tragedy led to widespread outrage and significant changes in UK policy on waste management. Aberfan remains a symbol of one of the UK's worst industrial disasters."],
["Six-Day War Begins","June","1967","The Six-Day War in June 1967 was a brief but intense conflict between Israel and a coalition of Arab states, including Egypt, Jordan, and Syria. Israel's swift victory altered the Middle East's geopolitical landscape, gaining control of the Gaza Strip, West Bank, and Golan Heights. This war had profound implications for the region's ongoing conflicts."],
["Grosvenor Square Anti-Vietnam Riots","March","1968","In March 1968, a large anti-Vietnam War demonstration in London's Grosvenor Square turned violent. Protesters clashed with police outside the US Embassy, reflecting growing opposition to the Vietnam War in the UK. This event was part of a global wave of protests against the Vietnam War."],
["Paris Riots - France Comes Close To Revolution","May","1968","In May 1968, massive student-led demonstrations and general strikes brought France to a standstill. The protests sparked by university disputes quickly gained momentum, challenging the government and societal norms. These events represented a significant moment of cultural and political upheaval in France."],
["Soviets Put Down Prague Spring","August","1968","The Prague Spring, a period of political liberalization in Czechoslovakia, was forcefully ended by a Soviet-led invasion in August 1968. This intervention suppressed the reform movement and reinstated hardline Communist rule. The Prague Spring and its suppression had a lasting impact on Cold War politics."],
["Concorde Flies For First Time","March","1969","The Concorde, a supersonic passenger airliner, made its first flight in March 1969. This aircraft, developed jointly by Britain and France, revolutionized air travel with its speed. The Concorde became a symbol of luxury and technological achievement."],
["Armstrong Sets Foot On The Moon","July","1969","In July 1969, Neil Armstrong became the first person to walk on the moon during the Apollo 11 mission. This monumental event marked a significant achievement in space exploration and the culmination of the US space race against the Soviet Union. Armstrong's famous words, \"That's one small step for man, one giant leap for mankind,\" captured the historical importance of the moment."],
["Watergate Scandal","June","1972","The Watergate scandal, beginning in June 1972, involved a break-in at the Democratic National Committee headquarters and the subsequent cover-up by the Nixon administration. The scandal led to President Nixon's resignation in 1974. Watergate had a lasting impact on American politics, leading to increased scrutiny of political activities."],
["First Cell Phone Call","April","1973","The first mobile phone call was made by Martin Cooper, a Motorola engineer, in April 1973. This event marked the birth of the cellular mobile phone technology that would transform global communication. The call symbolized the beginning of the mobile telecommunications revolution."],
["Battle of the Sexes Tennis Match","September","1973","In September 1973, the \"Battle of the Sexes\" tennis match took place between Billie Jean King and Bobby Riggs. King's victory over Riggs was more than a sporting event; it was a significant moment in the women's rights movement. The match represented a triumph over gender stereotypes and inequalities in sports."],
["Invention of TCP/IP (Birthday of the Internet)","January","1983","In January 1983, the adoption of TCP/IP protocols marked the birth of the modern Internet. This technology laid the foundation for global digital communication and the vast network we know today. The implementation of TCP/IP was a critical step in the development of the Internet."],
["The Space Shuttle Challenger Disaster","January","1986","The Space Shuttle Challenger disaster occurred in January 1986 when the shuttle broke apart shortly after launch, killing all seven crew members. This tragedy was a significant setback for the US space program and raised questions about the safety of space travel. The disaster led to a reevaluation of NASA's policies and procedures."],
["Soviet Nuclear Reactor at Chernobyl Explodes","April","1986","In April 1986, the Chernobyl nuclear power plant in the Soviet Union suffered a catastrophic meltdown, causing the worst nuclear disaster in history. The explosion released massive amounts of radioactive material into the environment. The Chernobyl disaster had widespread health and environmental impacts and highlighted the risks of nuclear power."],
["Fall of the Berlin Wall","November","1989","The fall of the Berlin Wall in November 1989 symbolized the end of the Cold War and the division of East and West Germany. This event led to the reunification of Germany and marked a significant turning point in European history. The fall of the Wall was a momentous event in the struggle for freedom and democracy in Eastern Europe."]]

#Place your code here
for event in range(len(events)):
    print(event, events[event])

