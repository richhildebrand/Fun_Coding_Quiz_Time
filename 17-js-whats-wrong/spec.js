describe("Test method should", function() {
  
    it("return given word", function() {
        var word = 'foo-bar';
        let result = testMethod(word);
        expect(result).toBe(word);
    });
});
  