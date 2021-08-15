const clearBtn = $('#clear-grid')
const saveBtn = $('#save-grid')
const colorInput = $('#color-picker');
const pixelCanvas = $('#pixel-canvas');



// Event listeners for grid-building buttons
let clickAndHold;

const rows = 32;
const columns = 64;


// Disable context menu on grid
pixelCanvas.contextmenu(function () {
    return false;
});

// Construct grid
function makeGrid() {
    for (let r = 1; r <= rows; r++) {
        const addRow = $("<tr></tr>");
        pixelCanvas.append(addRow);
        for (let c = 1; c <= columns; c++) {
            const addColumn = $("<td></td>");
            addRow.append(addColumn);
        }
    }
}


// Clear grid
function removeGrid() {
    pixelCanvas.children().remove();
}

function clearGrid() {
    removeGrid();
    makeGrid();
}

clearBtn.click(clearGrid);

let defaultColor = colorInput.val('#4286f4');

// Convert hex to rgb
function hexToRgb(hex) {
    hex = hex.replace('#', '');
    r = parseInt(hex.substring(0, hex.length / 3), 16);
    g = parseInt(hex.substring(hex.length / 3, 2 * hex.length / 3), 16);
    b = parseInt(hex.substring(2 * hex.length / 3, 3 * hex.length / 3), 16);

    result = `rgb(${r}, ${g}, ${b})`;
    return result;
};

// Color on single click. If same color erase
function draw() {
    let selectedColor = colorInput.val();
    $(this).css("background-color") == hexToRgb(selectedColor) ?
        $(this).css('background-color', '') : $(this).css('background-color', selectedColor);
};

// click and drag draw/erase function
function drag() {
    let mouseIsDown = true;
    let clicks = $(this).data('clicks');
    pixelCanvas
        .on('mouseleave', 'td', function () {
            if (mouseIsDown) {
                if (!clicks) {
                    // Change background color of cell
                    $(this).css('background-color', colorInput.val());
                } else {
                    // On second click return color to default (erase)
                    $(this).css('background-color', '');
                }
                // Fire `if` event on odd clicks
                $(this).data('clicks', !clicks);
            }
        })
        .on('mousedown', 'td', function () {
            event.preventDefault();
            mouseIsDown = true;
        })
        .on('mouseup', 'td', function () {
            mouseIsDown = false;
        });
    pixelCanvas.on('mouseleave', function () {
        mouseIsDown = false;
    });
}

// Event listener click delegated
pixelCanvas
    .on('mousedown', 'td', draw)
    .on('mousedown', 'td', drag);


var data = []

function save() {
    data = []
    $("#pixel-canvas tr").each(function (y) {
        $("td", this).each(function (x) {
            if ($(this).css('background-color') == "rgba(0, 0, 0, 0)") {
                data.push(`${x}, ${y}, 0, 0, 0`);
            } else {
                data.push(`${x}, ${y}, ${$(this).css('background-color').replace("rgb(", "").replace(")", "")}`);
            }
        });
    });
    update(data)
}
function update(data) {
    $(document).ready(function () {

        var js_data = JSON.stringify(data);
        $.ajax({
            url: '/',
            type: 'post',
            contentType: 'application/json',
            dataType: 'json',
            data: js_data
        }).done(function (result) {
            $("#data").html(result);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            console.log("fail: ", textStatus, errorThrown);

        });
    });
}

saveBtn.click(save);

makeGrid()

