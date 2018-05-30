describe("Test method should", function() {
    let _dom = undefined;

    beforeEach(function() {
        _dom = document.createElement("section");
        _addButton(_dom, 'btn-0', 'Button 1!')
        _addButton(_dom, 'btn-1', 'Button 2!')
        _addButton(_dom, 'btn-2', 'Button 3!')
    });

    let _addButton = function(parent, id, text) {
        var button = document.createElement("button");
        button.setAttribute("id", id);
        button.innerHTML = text;
        parent.appendChild(button);
    } 

    it("click our first button", function() {
        attachListeners(_dom)
        _dom.querySelector('#btn-0').click();
    });

    it("click our first button", function() {
        workingAttachListeners(_dom)
        _dom.querySelector('#btn-0').click();
    });
});
  