const speeds: number[] = [60, 80, 45, 90, 70, 55];
function avgSpeed(values: number[]): number {
    let sum: number = 0;
    let count: number = 0;

    for (const value of values) {
        sum += value;
        count++;
    }

    return sum / count;
}
const averageSpeed: number = avgSpeed(speeds);
console.log("Средняя скорость: " + averageSpeed);
