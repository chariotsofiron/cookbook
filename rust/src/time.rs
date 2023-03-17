use std::time::{SystemTime, UNIX_EPOCH};

/// Gets the current time in microseconds
pub fn current_time_micros() -> u64 {
    u64::try_from(
        SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .expect("Current time is before UNIX epoch")
            .as_micros(),
    )
    .expect("Current time is too large to fit in u64")
}
