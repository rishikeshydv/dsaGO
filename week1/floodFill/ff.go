package floodFill

func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	oldColor := image[sr][sc]
	if oldColor != newColor {
		dfs(image, sr, sc, oldColor, newColor)
	}
	return image
}

func dfs(image [][]int, sr int, sc int, oldColor int, newColor int) {
	if sr < 0 || sr >= len(image) || sc < 0 || sc >= len(image[0]) || image[sr][sc] != oldColor {
		return
	}
	image[sr][sc] = newColor
	dfs(image, sr-1, sc, oldColor, newColor)
	dfs(image, sr+1, sc, oldColor, newColor)
	dfs(image, sr, sc-1, oldColor, newColor)
	dfs(image, sr, sc+1, oldColor, newColor)
}
