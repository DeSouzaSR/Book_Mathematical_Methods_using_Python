function seq = fibonacci(n)
  if (nargin != 1)
    usage('fibonacci(num_terms)');
  endif

  seq = ones(1, n);
  for term = 3:n
    seq(term) = seq(term - 1) + seq(term - 2);
  endfor
end

