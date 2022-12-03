use std::fs;

pub fn solve() {
    let input = fs::read_to_string("inputs/day01.txt").expect("error while opening the input");
    
    let calories: Vec<i32> = input.split("\r\n\r\n")
                                    .map(|x| x.split("\r\n")
                                        .map(|y| y.parse::<i32>().unwrap())
                                        .sum::<i32>())
                                    .collect();

    let mut maxis = [0, 0, 0];
    for cal in calories.iter() {
        let min = maxis.iter().min().unwrap();
        if cal > min {
            maxis[maxis.iter().position(|r| r == min).unwrap()] = *cal;
        }
    }

    println!("Part one ==> {} \r\nPart two ==> {}", maxis.iter().max().unwrap(), maxis.iter().sum::<i32>());
}