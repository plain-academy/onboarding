use base32;
use rand::{rngs::OsRng, RngCore, SeedableRng};
use rand_chacha::ChaChaRng;
use std::error::Error;
use structopt::StructOpt;

fn main() {
    PwGen::from_args().exec().unwrap_or_else(print_error)
}

fn print_error<'a>(error: Box<dyn Error + 'a>) {
    eprintln!("{}", error);
    match error.source() {
        Some(source_err) => {
            eprintln!("  --> {}", source_err);
            print_error(Box::new(source_err))
        }
        None => std::process::exit(1),
    }
}

#[derive(StructOpt)]
#[structopt(rename_all = "kebab-case")]
#[derive(Debug)]
pub struct PwGen {
    /// Display the characters in lower case
    #[structopt(long = "lower", short = "l")]
    lower: bool,
    /// The number of characters to print
    /// must be a multiple of 8 (e.g 8, 16, 32)
    #[structopt(long = "num", short = "n", default_value = "32")]
    num: u32,
}

impl PwGen {
    pub fn exec(self) -> Result<(), Box<dyn Error>> {
        match self.num % 8 {
            0 => {
                let pw = gen_base32_pw(self.num)?;
                match self.lower {
                    true => println!("{}", pw.to_lowercase()),
                    false => println!("{}", pw.to_uppercase()),
                }
                Ok(())
            }
            _ => Err(Box::new(CliFlagValidationError::InvalidNum)),
        }
    }
}

fn gen_base32_pw(num: u32) -> Result<String, Box<dyn Error>> {
    let mut rng = ChaChaRng::from_rng(OsRng)?;
    let mut pw_bytes = vec![0; (num / 8 * 5).try_into()?].into_boxed_slice();
    rng.fill_bytes(&mut pw_bytes);
    let base32_pw = base32::encode(base32::Alphabet::RFC4648 { padding: false }, &pw_bytes);
    Ok(base32_pw)
}

#[derive(Debug, thiserror::Error)]
pub enum CliFlagValidationError {
    #[error("number of chars must be a multiple of 8")]
    InvalidNum,
}
