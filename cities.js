var state_arr = new Array(4: ('nv', 'Melanocytic nevi', ['Sensitivity to touch around the mole', 'Redness or inflammation around the mole'],['Avoid tight Clothing','Limit exposure to direct sunlight']),
    6: ('mel', 'Melanoma', ['Multiple colors within a mole', 'Bleeding or oozing from a mole'],['Eat a balanced diet rich in antioxidants and vitamins','Avoid smoking and limit alcohol consumption']),
    2: ('bkl', 'Benign keratosis-like lesions',  ['Itching or irritation in affected areas, Round or oval shaped growths', 'Very small growths clustered around the eyes or elsewhere on the face'],['Moisturize Regularly','Manage Stress by meditation or yoga']),
    1: ('bcc', 'Basal cell carcinoma', ['Surrounding skin becoming sunken or depressed','Formation of a flesh-coloured, pearl like bump'],['Avoid harmful chemicals','Wear Protective Clothing']),
    5: ('vasc', 'Pyogenic granulomas and hemorrhage', ['Prone to Ulceration', 'Moist or friable surface structure'],['Use sunscreen with a high SPF','Keep the affected arear covered with a sterile dressing']),
    0: ('akiec', 'Actinic keratoses and intraepithelial carcinomae', ['Swelling and burning in affected region', 'Thickening of the skin'],['Avoid tanning beds and sunlamps','Avoid hot shower and opt for lukewarm water']),
    3: ('df', 'Dermatofibroma', ['Dimpled appearance when pressed', 'Growing in size over time'],['Avoid using harsh chemicals or irritants','Drink plenty of water and maintain proper hydration']) 
    );

var s_a = new Array();
s_a[1]="Melanocytic nevi";
s_a[2]="Melanoma"; 
s_a[3]="Benign keratosis-like lesions";
s_a[4]="Basal cell carcinoma";
s_a[5]="Pyogenic granulomas and hemorrhage";
s_a[6]="Actinic keratoses and intraepithelial carcinomae";
s_a[7]="Dermatofibroma";


function printDisease(diseaseId) {
    // given the id of the <select> tag as function argument, it inserts <option> tags
    var optionStr = document.getElementById(diseaseId);
    optionStr.length = 0;
    optionStr.options[0] = new Option('Select Skin Disease', '');
    optionStr.selectedIndex = 0;
    for (var i = 0; i < diseaseArr.length; i++) {
        optionStr.options[optionStr.length] = new Option(diseaseArr[i], diseaseArr[i]);
    }
}

// Assuming you have a variable containing the disease names
var diseaseArr = ['Melanocytic nevi', 'Melanoma', 'Benign keratosis-like lesions', 'Basal cell carcinoma', 'Pyogenic granulomas and hemorrhage', 'Actinic keratoses and intraepithelial carcinomae', 'Dermatofibroma'];

printDisease('diseaseSelect'); // Call this function to populate the disease select dropdown

function predictDisease() {
    var selectedDisease = document.getElementById('diseaseSelect').value;
    // Here, you can perform actions based on the selected disease, like fetching data from the server
    // and displaying the prediction results.
    alert('You selected: ' + selectedDisease); // For demonstration, alert the selected disease
}

// Example HTML for the select dropdown and button:
/*
<select id="diseaseSelect"></select>
<button onclick="predictDisease()">Predict Disease</button>
*/
