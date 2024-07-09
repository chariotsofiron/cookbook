// these should be sorted by length for maximal munch
const OPERATORS: [(&str, usize); 18] = [
    ("||", 0),
    ("&&", 1),
    ("==", 2),
    ("!=", 2),
    ("<=", 2),
    (">=", 2),
    ("<<", 9),
    (">>", 9),
    ("<", 2),
    (">", 2),
    ("|", 3),
    ("^", 4),
    ("&", 5),
    ("+", 10),
    ("-", 10),
    ("*", 20),
    ("/", 20),
    ("%", 20),
];

pub fn parse(input: &str) -> Result<u64, String> {
    let mut parser = Parser::new(input);
    let result = parser.parse_expression(0);
    if parser.i < parser.input.len() {
        Err(format!(
            "Unexpected input at position {}: {}",
            parser.i,
            &parser.input[parser.i..]
        ))
    } else {
        result
    }
}

struct Parser<'a> {
    input: &'a str,
    i: usize,
}

impl<'a> Parser<'a> {
    pub fn new(input: &'a str) -> Self {
        Parser { input, i: 0 }
    }

    fn accept(&mut self, tok: &str) -> bool {
        if self.input[self.i..].starts_with(tok) {
            self.i += tok.len();
            true
        } else {
            false
        }
    }

    fn accept_number(&mut self) -> Option<u64> {
        if self.input[self.i..].starts_with(char::is_numeric) {
            let start = self.i;
            while self.input[self.i..].starts_with(char::is_numeric) {
                self.i += 1;
            }
            let num = &self.input[start..self.i];
            Some(num.parse().unwrap())
        } else {
            None
        }
    }

    fn expect(&mut self, tok: &str) -> Result<(), String> {
        if self.accept(tok) {
            Ok(())
        } else {
            Err(format!("Expected {} {}", tok, &self.input[self.i..]))
        }
    }

    pub fn parse_expression(&mut self, precedence: usize) -> Result<u64, String> {
        let mut left = self.parse_factor()?;

        while let Some((op, prec)) = OPERATORS
            .iter()
            .find_map(|(x, y)| self.input[self.i..].starts_with(x).then_some((*x, *y)))
        {
            if prec < precedence {
                break;
            }
            self.accept(op);
            let right = self.parse_expression(prec + 1)?;

            left = match op {
                "+" => left.wrapping_add(right),
                "-" => left.wrapping_sub(right),
                "*" => left.wrapping_mul(right),
                "/" => left.wrapping_div(right),
                "%" => left.wrapping_rem(right),
                "&" => left & right,
                "|" => left | right,
                "^" => left ^ right,
                "<<" => left.wrapping_shl(right as u32),
                ">>" => left.wrapping_shr(right as u32),
                "<" => u64::from(left < right),
                ">" => u64::from(left > right),
                "<=" => u64::from(left <= right),
                ">=" => u64::from(left >= right),
                "==" => u64::from(left == right),
                "!=" => u64::from(left != right),
                "&&" => u64::from(left != 0 && right != 0),
                "||" => u64::from(left != 0 || right != 0),
                _ => unreachable!(),
            };
        }
        Ok(left)
    }

    fn parse_factor(&mut self) -> Result<u64, String> {
        if self.accept("(") {
            let result = self.parse_expression(0)?;
            self.expect(")")?;
            Ok(result)
        } else if self.accept("-") {
            self.parse_factor().map(|x| (!x).wrapping_add(1)) // negate by 2s complement
        } else if let Some(number) = self.accept_number() {
            Ok(number)
        } else if self.i >= self.input.len() {
            Err("Unexpected end of input".to_string())
        } else {
            Err(format!(
                "Expected number or identifier {}",
                &self.input[self.i..]
            ))
        }
    }
}

#[cfg(test)]
mod tests {
    use super::parse;

    #[test]
    fn test0() {
        let input = "1";
        let result = parse(&input);
        assert_eq!(result, Ok(1));
    }

    #[test]
    fn test_negate_atom() {
        let input = "-1";
        let result = parse(&input);
        assert_eq!(result, Ok(!1 + 1));
    }

    #[test]
    fn test1() {
        let input = "1+2*3";
        let result = parse(&input);
        assert_eq!(result, Ok(7));
    }

    #[test]
    fn test2() {
        let input = "a";
        let result = parse(&input);
        assert_eq!(result, Err("Unexpected input at position 0: a".to_string()));
    }
}

//     #[test]
//     fn test2() {
//         let input = "10 >> 1 == 0";
//         let map = HashMap::new();
//         let result = parse(&input, &map, false);
//         assert_eq!(result, Ok(0));
//     }

//     #[test]
//     fn test3() {
//         let input = "12 >> 6 != 0 && (12 >> 6) & 1023 != 1023";
//         let map = HashMap::new();
//         let result = parse(&input, &map, false);
//         assert_eq!(result, Ok(0));
//     }

//     #[test]
//     fn test4() {
//         let input = "23#";
//         let map = HashMap::new();
//         let result = parse(&input, &map, false);
//         assert_eq!(result, Err("Unexpected input at position 2: #".to_string()));
//     }
// }
