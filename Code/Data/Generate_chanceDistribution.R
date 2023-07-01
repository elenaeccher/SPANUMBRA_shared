library(pracma) #to perform permutations

arr <- array(1:10, dim = c(1,10)) # array of 10 positions

# Transpose the array
new_arr <- t(arr)

null_x = perms(new_arr) # all possible permutation of the 1-10 numerosities over 10 positions

# Initialize vectors
r <- numeric(nrow(null_x))
pr <- numeric(nrow(null_x))

# Loop through rows of null_x
for (n in 1:nrow(null_x)) {
  # Calculate correlation using Kendall's method
  cor_res <- cor.test(null_x[n,], new_arr, method = "kendall") #Kendall tau for each possible permutations with a ordered 1 to 10 array
  
  # Store correlation coefficient and p-value
  r[n] <- cor_res$estimate
  pr[n] <- cor_res$p.value
}

save(r,null_x,cor_res, file = "./Permutation_Distr.Rdata")
