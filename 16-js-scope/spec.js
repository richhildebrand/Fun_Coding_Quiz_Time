describe("Test method should", function() {
  
    it("return given word", function() {
        let outsideWord = 'outside';
        let insideWord = 'inside';

        let result = poor_naming_conventions(outsideWord, insideWord);

        expect(result).toBe(undefined);
    });
});
  