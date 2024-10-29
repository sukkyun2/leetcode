class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        for(int i=0;i<flowerbed.length;i++){
            if(flowerbed[i] == 1) continue;

            if(canPlant(flowerbed, i-1) && canPlant(flowerbed, i+1)){
                flowerbed[i] = 1;
                n-=1;
            }
        }

        return n <= 0;
    }

    private boolean canPlant(int[] flowerbed, int i){
        if(i<0 || i > flowerbed.length - 1) return true;

        return flowerbed[i] == 0;
    }
}